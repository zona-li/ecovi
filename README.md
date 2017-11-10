# EcoVi

The website discovers and markets the best and most responsible products and companies that are building towards a sustainable future or lifestyle.

Features
------------

- Search
- Sign up and sign in with email confirmation
- List of people to work with and products to buy

Installation
------------

Run: "docker-compose up" in Terminal

App Structure
------------

* Project name: homestarter
* Django apps: main, search
* REST API app: api



Tech Stack
------------
Application and Data:
- Python
- Django
- MySQL  
NoSQL was born with the backdrop of our need to store and process data generated at higher volumes and velocities than ever before. However developers find it increasingly difficult to connect those databases to applications. They need to write glue code to kludge together NoSQL tools, learn a myriad of new languages, and because of the lackage of third party ecosystem, companies need to develop their own operational and visualization tools. The lack of JOINs also led to denormalization, which led to data bloat and rigidity. Startups using NoSQL at first often times found themselves returning back to SQL later on. SQL is a standardize and robust query language. Now it (such as CockroachDB) can do fast ingest and complex queries, it is much more scalable as it is before, and it interfaces on top of Hadoop and Spark so we can use those data processing tools on structured data.
- JavaScript
- Bootstrap
- jQuery
- Sass
- Vue.js

Utilities:
- Google analytics
- Mailchimp: for marketing emails

DevOps:
- Docker  
Reasoning: Portability: it ensures the deployment environment is exactly the same as the development environment. Easy to set up top-level architecture: One invocation of docker-compose will have Docker setup everything - it provides a simple description of how runtime components talk to each other. Docker has its own clustering systems Docker Swarm. Inherent security due to isolation.
- Git  
- uWSGI(Web Server Gateway Interface)  
A Python WSGI HTTP Server. Can serve as the dynamic interpreter for Nginx. uWSGI from a number of benchmarks has shown to be the fastest server for python applications and allows lots of flexibility. Nginx has become the standard for serving up web applications and has the additional benefit that it can talk to uWSGI using the uWSGI protocol, further eliminating overhead.  
the web client <-> the web server <-> the socket <-> uwsgi <-> Django
- Nginx  
A web server. Better performance than Apache when serving static content, designed for high number of concurrent requests.
- AWS Elastic Beanstalk  
Reasoning: Elastic Beanstalk supports Multi-Container-Environments, auto-scaling, and load balancing. Fast to setup. ECS offer finer control of the scaling and capacity, but is more expensive and has a steeper learning curve.


Business Tools:
- G-suite
- Slack
- Asana

Contribute
------------

- Source Code: https://github.com/ZonaClark/homestarter.git

Support
------------

If you are having issues, email us at: contact@ecovi.io

License
------------

The project is licensed under the BSD license.
