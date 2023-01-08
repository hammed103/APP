from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("phone number"), max_length=30, default="+250784123456"
    )

    country = CountryField(
        verbose_name=_("country"), default="USA", blank=False, null=False
    )

    job_role = models.CharField(verbose_name=_("job role"), max_length=60)
    
    city = models.CharField(
        verbose_name=_("city"),
        max_length=180,
        default="NEW YORK",
        blank=False,
        null=False,
    )
    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), default="/profile_default.png"
    )

    interests = models.ManyToManyField(
        "self", symmetrical=False, related_name="interests_follows", blank=True
    )

    bookmarked = models.ManyToManyField(
        "self", symmetrical=False, related_name="bookmarked_saved", blank=True
    )

    histories = models.ManyToManyField(
        "self", symmetrical=False, related_name="histories_visited", blank=True
    )

    def __str__(self):
        return f"{self.user.get_name_abbrev()}"

    def interests_list(self):
        return self.interests.all()

    def interest(self, institution):
        self.interest.add(institution)

    def disinterest(self, institution):
        self.interests.remove(institution)

    def bookmarked_list(self):
        return self.bookmarked.all()

    def bookmark(self, report):
        self.bookmark.add(report)

    def unbookmark(self, report):
        self.bookmarked.remove(report)

    def history_list(self):
        return self.histories.all()

    def clear_history(self, report):
        self.bookmarked.clear()
