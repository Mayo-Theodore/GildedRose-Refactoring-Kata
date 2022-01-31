import pytest
from gilded_rose import Item, GildedRose

@pytest.fixture
def new_list_of_items():
    '''Returns a list of items'''
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6)  
            ]
    return items

def test_create_new_item():
    '''Tests that an item can be created'''
    item = Item("Carrot", 5, 10)
    assert item.name == "Carrot"
    assert item.sell_in == 5
    assert item.quality == 10

def test_list_of_items(new_list_of_items):
    assert str(new_list_of_items[0]) == "+5 Dexterity Vest, 10, 20"
            


