# -*- coding: utf-8 -*-
class QualityControl(Exception):
    pass
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
class GildedRose(object):

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:

            '''Constants'''
            QUALITY_MAX = 50
            QUALITY_MIN = 0

            '''Check items meet quality requirements'''
            if QUALITY_MIN < item.quality > QUALITY_MAX:
                raise QualityControl("Sorry an item's quality must be between 0 and 50")

            '''Update item quality'''
            if "Aged Brie" not in item.name and "Sulfuras" not in item.name and "Backstage" not in item.name:
                if "Conjured" in item.name or item.sell_in < 0:
                    item.quality -= 2
                elif item.sell_in >= 0:
                    item.quality -= 1
                if item.quality < QUALITY_MIN:
                    item.quality = QUALITY_MIN

            '''Aged Brie quality'''
            if "Aged Brie" in item.name:
                if item.quality == QUALITY_MAX:
                    item.quality = item.quality
                elif item.quality < QUALITY_MAX:
                    item.quality += 1 

            '''Sulfuras quality '''
            if "Sulfuras" in item.name and QUALITY_MIN < item.quality > QUALITY_MAX:
                 item.quality = item.quality

            '''Backstage passes quality '''
            if "Backstage" in item.name and item.quality < QUALITY_MAX:
                if item.sell_in >= 15:
                    item.quality += 1
                if 10 <= item.sell_in < 15:
                    item.quality += 2
                if 5 <= item.sell_in < 10:
                    item.quality += 3
                if item.sell_in <= 0:
                    item.quality = QUALITY_MIN
            elif "Backstage" in item.name and item.quality >= QUALITY_MAX:
                item.quality = QUALITY_MAX
            
            '''Sell_in'''
            if "Sulfuras" in item.name:
                item.sell_in = None
            else:
                item.sell_in -= 1