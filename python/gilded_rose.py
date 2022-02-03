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

class ItemChecker(object):
    def __init__(self, items):
        self.items = items
        self.organised_items = {}
        self.general_items = []
        self.aged_brie = []
        self.sulfuras = []
        self.backstage = []
        self.conjured = []

    def check_quality(self):
        for item in self.items:
            '''Constants'''
            QUALITY_MAX = 50
            QUALITY_MIN = 0
            '''Check items meet quality requirements'''
            if QUALITY_MIN < item.quality > QUALITY_MAX:
                raise QualityControl("Sorry an item's quality must be between 0 and 50")
    
    def sort_items(self):
        '''Organises each item according to category'''
        for item in self.items:
            if "Aged Brie" in item.name:
                self.aged_brie.append(item)
                self.organised_items["Aged Brie"] = self.aged_brie
            elif "Sulfuras" in item.name:
                self.sulfuras.append(item)
                self.organised_items["Sulfuras"] = self.sulfuras
            elif "Backstage" in item.name:
                self.backstage.append(item)
                self.organised_items["Backstage"] = self.backstage
            elif "Conjured" in item.name:
                self.conjured.append(item)
                self.organised_items["Conjured"] = self.conjured
            elif "Aged Brie" not in item.name and "Sulfuras" not in item.name and "Backstage" not in item.name and "Conjured" not in item.name:
                self.general_items.append(item)
                self.organised_items["General Items"] = self.general_items
        return self.organised_items

class GildedRose(ItemChecker):
    def list_items(self):
        '''Displays available items in gilded rose'''
        return self.organised_items
             
    def update_sell_in(self):
        '''Update sell in value for all items'''
        for key,values in self.organised_items.items():
            for item in values:
                if "Sulfuras" in item.name:
                    item.sell_in = None
                else:
                    item.sell_in -= 1
        return self.organised_items
    
    def update_quality(self):
        '''Update quality score for all items'''
        for value in self.organised_items.values():
            for item in value:
                '''Constants'''
                QUALITY_MAX = 50
                QUALITY_MIN = 0

                '''Update Quality: General Items and Conjured Items'''
                if "Aged Brie" not in item.name and "Sulfuras" not in item.name and "Backstage" not in item.name:
                    if "Conjured" in item.name or item.sell_in < 0:
                        item.quality -= 2
                    elif item.sell_in >= 0:
                        item.quality -= 1
                    if item.quality < QUALITY_MIN:
                        item.quality = QUALITY_MIN

                '''Update Quality: Aged Brie'''
                if "Aged Brie" in item.name:
                    if item.quality == QUALITY_MAX:
                        item.quality = item.quality
                    elif item.quality < QUALITY_MAX:
                        item.quality += 1 

                '''Update Quality: Sulfuras'''
                if "Sulfuras" in item.name and QUALITY_MIN < item.quality > QUALITY_MAX:
                    item.quality = item.quality

                '''Update quality: Backstage passes'''
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
        return self.organised_items




