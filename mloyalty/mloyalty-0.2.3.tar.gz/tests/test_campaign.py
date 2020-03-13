from mloyalty.campaign import Campaign


class TestCampaign:
    def test_get_campaigns(self):
        campaign = Campaign()
        resp = campaign.get_campaigns()
        assert isinstance(resp, dict)

    def test_get_campaign(self):
        campaign = Campaign()
        resp = campaign.get_campaign(2)
        assert isinstance(resp, dict)
