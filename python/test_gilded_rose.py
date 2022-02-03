import pytest
from gilded_rose import Item, ItemChecker, GildedRose, QualityControl

def test_create_new_item():
    '''Tests that an item can be created'''
    item = Item("Carrot", 5, 10)
    assert item.name == "Carrot"
    assert item.sell_in == 5
    assert item.quality == 10

@pytest.fixture
def item_list():
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

def test_list_of_items(item_list):
    '''Tests that an individual item from the list of items can be accessed'''
    assert str(item_list[0]) == "+5 Dexterity Vest, 10, 20"

@pytest.fixture
def item_checker(item_list):
    '''Returns an instance of ItemChecker, with some items stored'''
    return ItemChecker(item_list)

def test_store_item_with_wrong_quality():
    '''Tests that items that fall outside the quality requirements get rejected '''
    with pytest.raises(QualityControl):
        items = [Item(name="Aged Brie", sell_in=2, quality=51), Item(name="Aged Brie", sell_in=2, quality=-1), Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=-5)]
        gilded = ItemChecker(items)
        gilded.check_quality()

def test_items_in_item_checker(item_checker, item_list):
    '''Tests items are stored and accessible in Item Checker'''
    assert item_checker.items == item_list
    assert item_checker.items[0].quality == 20

def test_organise_items(item_checker):
    '''Test that items are organised into relevant categories'''
    assert item_checker.sort_items()["General Items"] is not None

@pytest.fixture
def gilded_rose(item_list):
    '''Returns an instance of Gilded Rose'''
    return GildedRose(item_list)

def test_store_items_in_gilded_rose(gilded_rose):
    '''Checks items are stored and accesible in instance of Gilded Rose'''
    gilded_rose.sort_items()
    assert gilded_rose.list_items() is not None

def test_sell_in_date_decreases(gilded_rose):
    '''Tests sell_in value updates'''
    gilded_rose.sort_items()
    assert gilded_rose.update_sell_in()["Aged Brie"][0].sell_in == 1
    assert gilded_rose.organised_items["Conjured"][0].sell_in == 2

def test_sulfuras_sell_in():
    '''Tests sulfuras never has to be sold'''
    items = [
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=0),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=50)
        ]
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    assert gilded_rose.update_sell_in()["Sulfuras"][0].sell_in == None
    assert gilded_rose.organised_items["Sulfuras"][1].sell_in == None

def test_quality_decreases_faster_after_sell_by():
    '''Tests item quality decreases twice as fast after sell_in date'''
    items = [
    Item(name="+5 Dexterity Vest", sell_in=-1, quality=20), 
    Item(name="+5 Dexterity Vest", sell_in=5, quality=20) 
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    assert gilded_rose.update_quality()["General Items"][0].quality == 18
    assert gilded_rose.organised_items["General Items"][1].quality == 19

def test_quality_never_negative():
    '''Tests that the quality of an item never falls below zero'''
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=0), 
        Item(name="Elixir of the Mongoose", sell_in=5, quality=0), 
        Item(name="Conjured Mana Cake", sell_in=3, quality=0)
        ]
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    assert gilded_rose.update_quality()["General Items"][0].quality == 0
    assert gilded_rose.update_quality()["General Items"][1].quality == 0
    assert gilded_rose.update_quality()["Conjured"][0].quality == 0

def test_quality_limit():
    '''Tests that the quality never increases above 50'''
    items = [
    Item(name="Aged Brie", sell_in=2, quality=50), 
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    assert gilded_rose.update_quality()["Aged Brie"][0].quality == 50

def test_aged_brie_increases_quality():
    '''Tests that aged brie increases in quality'''
    items = [
    Item(name="Aged Brie", sell_in=2, quality=50), 
    Item(name="Aged Brie", sell_in=2, quality=0)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    assert gilded_rose.update_quality()["Aged Brie"][0].quality == 50
    assert gilded_rose.organised_items["Aged Brie"][1].quality == 1

def test_sulfuras_quality():
    '''Tests sulfuras quality does not decrease'''
    items = [
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=0),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=48)
        ]
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    assert gilded_rose.update_quality()["Sulfuras"][0].quality == 0
    assert gilded_rose.organised_items["Sulfuras"][1].quality == 48

def test_backstage_passes():
    '''Tests quality of backstage passes at different sell in times'''
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=30, quality=50) ]     
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    gilded_rose.update_quality()["Backstage"][0].quality == 21
    gilded_rose.organised_items["Backstage"][0].quality == 22
    gilded_rose.organised_items["Backstage"][0].quality == 23
    gilded_rose.organised_items["Backstage"][0].quality == 0
    gilded_rose.organised_items["Backstage"][0].quality == 0
    gilded_rose.organised_items["Backstage"][0].quality == 50

def test_conjured_quality():
    '''Tests “Conjured” items degrade in Quality twice as fast as normal items'''
    items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6), Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)
    gilded_rose.sort_items()
    gilded_rose.update_quality()["Conjured"][0].quality == 4
    gilded_rose.organised_items["Conjured"][0].quality == 19


