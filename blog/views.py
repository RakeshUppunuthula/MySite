from django.shortcuts import render
from datetime import date

# Create your views here.



all_post = [
    {
    "slug": "hike-in-the-mountains",
    "image": "mountainHike.jpg",
    "author": "Rakesh",
    "date": date(2025, 1, 19),
    "title": "mountain Hiking",
    "excerpt":"leave the busY life enjoy the view of mother nature",
    "content": """ Mountain hiking offers a thrilling opportunity to connect with nature, providing both breathtaking
        views and a sense of accomplishment with every step. The challenging terrain tests your physical 
        limits, fostering resilience as you climb higher. Fresh air and serene surroundings enhance mental 
        clarity and rejuvenate the body.

        Every hike strengthens your body and mind, boosting endurance, flexibility, and cardiovascular health. 
        From dense forests to rocky ridgelines, the diverse landscapes offer ever-changing beauty. As you 
        ascend, the peace of the mountains offers an escape from the chaos of everyday life.

        The rewards of hiking go beyond physical fitness, offering a chance for reflection and immersion in
        the natural world. The sense of freedom that comes with reaching the summit is unmatched, 
        teaching the value of perseverance. Each hike is a personal journey that deepens your connection to
        nature and fosters growth.
        """
    },

    {
    "slug": "Programming",
    "image": "programming.jpg",
    "author": "Rakesh",
    "date": date(2024, 1, 19),
    "title": " code is fun",
    "excerpt":"practice makes man perfect",
    "content": """Programming is a skill that lets you create and solve problems through code, enhancing your logical thinking.
      With each line, you gain a deeper understanding of technology and its possibilities. The process is rewarding as you watch 
      your code come to life.

      Learning different programming languages introduces new tools and techniques to tackle problems creatively. Whether it’s Python 
      or JavaScript, each language offers unique solutions. The challenges may be tough, but the sense of accomplishment is worth it.

      In programming, learning never stops as new tools and frameworks emerge. Staying updated ensures your skills evolve with technology,
      keeping you relevant in the fast-paced world of software development.
        """


    },

    {
    "slug": "snow",
    "image": "snow.jpg",
    "author": "Rakesh",
    "date": date(2023, 1, 19),
    "title": "White is peace",
    "excerpt":"Beatuy of Nature-- explore... enjoy...alive..",
    "content": """ Snow transforms the landscape into a serene, white wonderland, creating a peaceful, magical atmosphere. The quiet of falling snow 
        enhances the beauty of the surroundings, turning ordinary views into extraordinary sights. Snow-covered mountains and forests offer breathtaking 
        contrasts of white against dark trees or clear skies.

        The view of snow brings a sense of purity and tranquility, offering a moment to pause and appreciate nature. Snow’s gentle fall creates a calm,
        refreshing feeling that captivates the senses. It’s a reminder of nature’s simplicity and the quiet beauty found in winter landscapes.
        """


    }
]


def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts=sorted(all_post,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html", {"posts":latest_posts})

def posts(request):
    return render(request,"blog/all-posts.html", {"all_posts":all_post})

def post_detail(request,slug):
    identitfied_post =  next(post for post in all_post if post['slug']==slug)
    return render(request,"blog/post-detail.html" , {"post":identitfied_post})
    
