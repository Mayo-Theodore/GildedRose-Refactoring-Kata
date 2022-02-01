import pytest
from gilded_rose import Item, GildedRose, QualityControl

def test_create_new_item():
    '''Tests that an item can be created'''
    item = Item("Carrot", 5, 10)
    assert item.name == "Carrot"
    assert item.sell_in == 5
    assert item.quality == 10

@pytest.fixture
def new_list_of_items():
    '''Returns a list of items'''
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=50),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=0),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6)  
            ]
    return items

def test_list_of_items(new_list_of_items):
    '''Tests that an individual item from the list of items can be accessed'''
    assert str(new_list_of_items[0]) == "+5 Dexterity Vest, 10, 20"

@pytest.fixture
def gilded_rose(new_list_of_items):
    '''Returns items stored in gilded rose'''
    return GildedRose(new_list_of_items)

def test_items_in_gilded_rose(gilded_rose, new_list_of_items):
    '''Tests items are stored and accessible in gilded rose'''
    assert gilded_rose.items == new_list_of_items
    assert gilded_rose.items[0].quality == 20

def test_sell_in_date_decreases(gilded_rose):
    '''Tests that sell in date decreases after update quality '''
    gilded_rose.update_quality()
    assert gilded_rose.items[0].sell_in == 9
    assert gilded_rose.items[1].sell_in == 1
    assert gilded_rose.items[3].sell_in == None
    assert gilded_rose.items[4].sell_in == None

def test_quality_decreases_faster_after_sell_by():
    '''Tests item quality decreases twice as fast after sell by date'''
    items = [Item(name="+5 Dexterity Vest", sell_in=-1, quality=20), Item(name="+5 Dexterity Vest", sell_in=0, quality=20), Item(name="+5 Dexterity Vest", sell_in=1, quality=20) ]
    gilded = GildedRose(items)
    gilded.update_quality()
    assert gilded.items[0].quality == 18
    assert gilded.items[1].quality == 19
    assert gilded.items[2].quality == 19


def test_store_item_with_wrong_quality():
    '''Tests that items that fall outside the quality requirements get rejected '''
    with pytest.raises(QualityControl):
        items = [Item(name="Aged Brie", sell_in=2, quality=51), Item(name="Aged Brie", sell_in=2, quality=-1)]
        gilded = GildedRose(items)
        gilded.update_quality()

def test_aged_brie_increases_quality():
    '''Tests that aged brie increases in quality'''
    items = [Item(name="Aged Brie", sell_in=2, quality=50), Item(name="Aged Brie", sell_in=2, quality=0)]
    gilded = GildedRose(items)
    gilded.update_quality()
    assert gilded.items[0].quality == 50
    assert gilded.items[1].quality == 1


def test_quality_never_negative():
    '''Tests that the quality of an item never falls below zero'''
    items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=-5), Item(name="Elixir of the Mongoose", sell_in=5, quality=0)]
    gilded = GildedRose(items)
    gilded.update_quality()
    assert gilded.items[0].quality == 0
    assert gilded.items[1].quality == 0

def test_quality_limit():
    '''Tests that the quality never increases above 50'''
    items = [Item(name="Aged Brie", sell_in=2, quality=50)]
    gilded = GildedRose(items)
    gilded.update_quality()
    assert gilded.items[0].quality == 50

def test_sulfuras_quality():
    '''Tests sulfuras quality does not decrease'''
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=0),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=50)]
    gilded = GildedRose(items)
    gilded.update_quality()
    assert gilded.items[0].quality == 0
    assert gilded.items[1].quality == 50

def test_sulfuras_sell_in():
    '''Tests sulfuras never has to be sold'''
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=0),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=50)]
    gilded = GildedRose(items)
    gilded.update_quality()
    assert gilded.items[0].sell_in == None
    assert gilded.items[1].sell_in == None

def test_backstage_passes():
    '''Tests quality of backstage passes at different sell in times'''
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=30, quality=50) ]     
    gilded = GildedRose(items)
    gilded.update_quality()
    assert gilded.items[0].quality == 21
    assert gilded.items[1].quality == 22
    assert gilded.items[2].quality == 23
    assert gilded.items[3].quality == 0
    assert gilded.items[4].quality == 0
    assert gilded.items[5].quality == 50

# def test_conjured_quality():
#     '''Tests “Conjured” items degrade in Quality twice as fast as normal items'''
#     items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
#     gilded = GildedRose(items)
#     gilded.update_quality()
#     assert gilded.items[0].quality == 4











