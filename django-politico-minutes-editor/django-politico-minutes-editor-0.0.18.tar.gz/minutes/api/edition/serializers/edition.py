from minutes.models import Edition
from rest_framework import serializers
from .minute import MinuteSerializer
from .sponsor import SponsorSerializer
from .vertical import VerticalSerializer
from .interstitial_instance import InterstitialInstanceSerializer


class EditionSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()
    is_latest_live = serializers.SerializerMethodField()
    byline = serializers.SerializerMethodField()
    sponsor = SponsorSerializer()
    vertical = VerticalSerializer()

    def get_is_latest_live(self, obj):
        return obj == Edition.objects.latest_live(obj.vertical)

    def get_cards(self, obj):
        minutes = self.get_minutes(obj)
        interstitials = self.get_interstitials(obj)

        cards = minutes + interstitials
        return cards

    def get_minutes(self, obj):
        minutes = obj.minutes.filter(type__is_meta=False)
        return MinuteSerializer(minutes, many=True).data

    def get_interstitials(self, obj):
        interstitials = obj.interstitials.all()
        return InterstitialInstanceSerializer(interstitials, many=True).data

    def get_meta(self, obj):
        minutes = obj.minutes.filter(type__is_meta=True)
        return MinuteSerializer(minutes, many=True).data

    def get_byline(self, obj):
        return set(
            [
                "{} {}".format(
                    minute.author.user.first_name, minute.author.user.last_name
                )
                for minute in obj.minutes.all()
            ]
        )

    class Meta:
        model = Edition
        fields = (
            "id",
            "theme",
            "vertical",
            "is_latest_live",
            "live",
            "publish_datetime",
            "byline",
            "sponsor",
            "cards",
            "meta",
        )
