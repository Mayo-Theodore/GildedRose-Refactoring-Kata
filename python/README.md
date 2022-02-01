# Gilded Rose Tech Test

This is a tech test which I have completed in order to improve my ability to read, refactor and extend legacy code. 

This project was completed using Python, and the tests were written using Pytest.

## User Stories

* All items have a Sell In value which denotes the number of days we have to sell the item. All items have a Quality value which denotes how valuable the item is. At the end of each day our system lowers both values for every item
* Once the sell by date has passed, Quality degrades twice as fast
* The Quality of an item is never negative
* “Aged Brie” actually increases in Quality the older it gets
* The Quality of an item is never more than 50
* “Sulfuras”, being a legendary item, never has to be sold or decreases in Quality
* “Backstage passes”, like Aged Brie, increases in Quality as it’s Sell In value approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
* “Conjured” items degrade in Quality twice as fast as normal items
## Usage
Clone this repo, to ensure you have the files saved to your system
```python
from gilded_rose import Item, GildedRose, QualityControl
# Create a list of items. Each item must have a name, sell_in date, and quality score
items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0)]

# Create an instance of Gilded Rose, and store the items you created
gilded_rose = GildedRose(items)

# Use the update quality method, to keep your stored items up to date!
gilded_rose.update_quality()
```
## Testing
Make sure you are in the directory that contains the "test_gilded_rose.py" file, then type the following commands into your terminal
```bash
#Install pytest
pip install pytest

# Run tests
pytest
```

