import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    headers = {"Authorization": "Bearer " + os.getenv("PROXYCURL_API_KEY")}
    response = requests.get(
        api_endpoint,
        params={"linkedin_profile_url": linkedin_profile_url},
        headers=headers,
    )

    # response = requests.get(
    #     "<add github gist url with content for testing>"
    # )

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    for i in data['experiences']:
        i.pop('logo_url')

    for i in data['education']:
        i.pop('logo_url')

    data['experiences'] = [x for x in data['experiences'] if x['starts_at']['year'] > 2014]

    return data
