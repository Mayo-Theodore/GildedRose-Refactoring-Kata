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

            '''Check items meet quality requirements'''
            if 0 < item.quality > 50:
                raise QualityControl("Sorry an item's quality must be between 0 and 50")

            '''Update item quality'''
            if "Aged Brie" not in item.name and "Sulfuras" not in item.name and "Backstage" not in item.name:
                if item.sell_in < 0 or "Conjured" in item.name:
                    item.quality -= 2
                elif item.sell_in >= 0:
                    item.quality -= 1
                if item.quality < 0:
                    item.quality = 0

            '''Aged Brie quality'''
            if "Aged Brie" in item.name:
                if item.quality == 50:
                    item.quality = item.quality
                elif item.quality < 50:
                    item.quality += 1 

            '''Update Sulfuras quality '''
            if "Sulfuras" in item.name and 0 < item.quality > 50:
                 item.quality = item.quality

            '''Backstage passes quality '''
            if "Backstage" in item.name and item.quality < 50:
                if item.sell_in >= 15:
                    item.quality += 1
                if 10 <= item.sell_in < 15:
                    item.quality += 2
                if 5 <= item.sell_in < 10:
                    item.quality += 3
                if item.sell_in <= 0:
                    item.quality = 0
            elif "Backstage" in item.name and item.quality >= 50:
                item.quality = 50
            
            '''Update items sell_in'''
            if "Sulfuras" in item.name:
                item.sell_in = None
            else:
                item.sell_in -= 1
                
           
          
                            
            

            

            


    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 # if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                 if "Backstage" in item.name:
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1 #refactor to item.sell_in -= 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality 
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1


