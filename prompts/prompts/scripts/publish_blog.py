import os, requests
from dotenv import load_dotenv

load_dotenv()

def publish_blog(title, body_html, tags, image_url=None):
    url = f"https://{os.getenv('SHOPIFY_STORE_URL')}/admin/api/2024-01/blogs/{os.getenv('BLOG_ID')}/articles.json"
    headers = {
        "X-Shopify-Access-Token": os.getenv("SHOPIFY_ACCESS_TOKEN"),
        "Content-Type": "application/json"
    }
    
    payload = {
        "article": {
            "title": title,
            "body_html": body_html,
            "author": "Performance Team",
            "tags": ", ".join(tags),
            "published": False,  # Draft mode
            "image": {"src": image_url} if image_url else None
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f"✅ Published: {response.json()['article']['title']}")

if __name__ == "__main__":
    publish_blog(
        title="Test Blog Post",
        body_html="<p>Content here</p>",
        tags=["performance", "automation"]
    )
