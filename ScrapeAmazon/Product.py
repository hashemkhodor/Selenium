# -*- coding: utf-8 -*-
"""
Created on Mon May 23 13:50:11 2022

@author: Hashem
"""

class Product(object):
    def __init__(self,name,link=None,keyword=None,price=[],deliveryoptions=None,deliveryprice=['Unavailable'],deliverytime=['Unavailable'],overview='',features='',criticalreviews='',goodreviews='',generalreviews='',rating='',details=''):
        self.name=name
        self.price=price
        self.deliveryprice=deliveryprice
        self.deliverytime=deliverytime
        self.link=link
        self.keyword=keyword
        self.deliveryoptions=deliveryoptions
        self.overview=overview
        self.features=features
        self.goodreviews=goodreviews
        self.criticalreviews=criticalreviews
        self.overallrating=rating
        self.details=details
        self.generalreviews=generalreviews
            

    def deliverybreakdown(self):
        self.price=[]
        self.deliveryprice=[]
        self.deliverytime=[]
        if len(self.deliveryoptions) >=1 and type(self.deliveryoptions[0])==tuple:
            dp=[]
            dt=[]
            for pair in self.deliveryoptions:
                self.price.append(pair[0])
                
                for delivpair in pair[1]:
                    if type(delivpair)!= str:
                        if 'fastest' != delivpair[0]:
                            #product.deliveryprice.append(delivpair[0])
                            dp.append(delivpair[0])
                            dt.append(delivpair[1])
                            #product.deliverytime.append(delivpair[1])
                        else:
                            dp.append(None)
                            dt.append(delivpair[1]+"("+ delivpair[0] +")")
                           
                    else:
                        dp.append(None)
                        dt.append(delivpair)
                     
                if dp!=[]:
                    
                    self.deliveryprice.append(dp)
                if dt!=[]:
                    self.deliverytime.append(dt)
        else:
            self.price.append(self.deliveryoptions[0])
            self.deliveryprice.append(None)
            self.deliverytime.append(self.deliveryoptions[1])
                    
                    
        
