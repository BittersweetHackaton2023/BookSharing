from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.title


class Member(models.Model):
    email = models.EmailField(unique=True)
    mileage = models.IntegerField(default=100)


class Order(models.Model):
    isbn = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    mileage = models.PositiveIntegerField(default=0)

##경매에 사용하는 클래스
class Auction(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    minimum_bid = models.PositiveIntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

##경매에 참여하는 인원들을 관리하는 모델
class AuctionParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자와의 연결
    email = models.EmailField()
    mileage = models.IntegerField()
    auction_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Auction Participants"

    def __str__(self):
        return self.email
