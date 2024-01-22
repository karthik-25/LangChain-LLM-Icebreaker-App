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
    #     "https://gist.githubusercontent.com/karthik-25/ccce13c73e75d3e98295e91d49a76431/raw/42e040b05f32bc66f7fcc645953729aaebe9b542/karthik.json"
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

    return data
