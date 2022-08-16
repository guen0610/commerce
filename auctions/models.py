from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"

class Auction(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    category = models.ForeignKey(Category, 
                                blank=True, null=True, 
                                on_delete=models.SET_NULL, 
                                related_name="category")

    start_bid = models.DecimalField(max_digits=7, 
                                    decimal_places=2, 
                                    validators=[MinValueValidator(0.01)])

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidders")

    watchers = models.ManyToManyField(User, blank=True, related_name="watchlist")
    
    def __str__(self):
        return f"Auction #{self.id}: ({self.name}) ({self.user.username})"


class Bid(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction")
    
    class Meta:
        ordering = ('-amount',)

    def __str__(self):
        return f"Bid #{self.id}: {self.amount} on {self.auction.name} by {self.user.username}"

class Comment(models.Model):
    message = models.TextField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auctions")

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return f"Comment #{self.id}: {self.user.username} on {self.auction.item_name}: {self.message}"