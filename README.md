# EcoVi

The website matches local constructors/designers with project owners who want to build or rennovate thier rea estate properties.

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
- JavaScript
- Mod_WSGI
- AWS Elastic Beanstalk. Reasoning: Elastic Beanstalk supports Multi-Container-Environments, auto-scaling, and load balancing. Fast to setup. ECS offer finer control of the scaling and capacity, but is more expensive and has a steeper learning curve.
- Sass
- Vue.js

Utilities:
- Google analytics
- Mailchimp: for marketing emails
- Sendgrid: for transactional emails

DevOps:
- Docker
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
