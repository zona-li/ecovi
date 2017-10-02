# EcoVi

The website matches trustworthy local constructors/designers with project owners who want to build or rennovate thier real estate properties.

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
- Apache Mod_WSGI(Web Server Gateway Interface)
- AWS Elastic Beanstalk.  
Reasoning: Elastic Beanstalk supports Multi-Container-Environments, auto-scaling, and load balancing. Fast to setup. ECS offer finer control of the scaling and capacity, but is more expensive and has a steeper learning curve.
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
- Sendgrid: for transactional emails

DevOps:
- Docker.  
Reasoning: Portability: it ensures the deployment environment is exactly the same as the development environment. Easy to set up top-level architecture: One invocation of docker-compose will have Docker setup everything - it provides a simple description of how runtime components talk to each other. Docker has its own clustering systems Docker Swarm. Inherent security due to isolation.
- GitHub

Business Tools:
- G-suit
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
