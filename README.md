# LinkedIn Icebreaker App using LangChain and OpenAI's LLM

## Description
This project is a web application (Flask microframework) built on top of [LangChain](https://www.langchain.com/) that leverages OpenAI's Large Language Model (LLM), [GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo), to generate personalized ice breakers by analyzing LinkedIn profiles. It involves LangChain's agents and [ReAct framework](https://arxiv.org/pdf/2210.03629.pdf) to intelligently search Google for LinkedIn URL of an individual using [SerpApi](https://serpapi.com/), scrape LinkedIn data using [Proxycurl](https://nubela.co/proxycurl/), and craft descriptions and conversation starters tailored to an individual's professional background using GPT-3.5. The goal was to explore and build an LLM-powered application using LangChain's modular framework. You can check it out [here](https://llm-icebreaker.onrender.com/).

This project is part of "LangChain - Develop LLM powered applications with LangChain" Udemy course by [Eden Marco](https://www.linkedin.com/in/eden-marco/).

## Components Overview

- `app.py`: Flask application entry point, defining web routes.
- `ice_breaker.py`: Core module for generating ice breakers using LinkedIn data and LLMs.
- `linkedin.py` & `linkedin_lookup_agent.py`: Modules for LinkedIn profile scraping and data extraction.
- `output_parsers.py`: Defines structures for parsing and formatting the generated data.
- `tools.py`: Utility functions supporting the application's operations.
