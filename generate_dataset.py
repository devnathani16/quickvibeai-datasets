import json
import os
from pathlib import Path

# Categories and examples (40 each)
fluent_english = [
    "Could you please explain how to implement a binary search tree in Python?",
    "I'm interested in learning about the architectural differences between Microservices and Monoliths.",
    "Would you be able to provide a comprehensive guide on optimizing SQL queries for large datasets?",
    "What are the best practices for maintaining a scalable React application?",
    "I would like to understand the implications of using asynchronous programming in a high-concurrency environment.",
    "Can you detail the process of deploying a Docker container to an AWS EKS cluster?",
    "It would be beneficial to have a thorough comparison of various state management libraries in Flutter.",
    "How does the garbage collection mechanism work in Java, and what are its performance impacts?",
    "I'm looking for an in-depth analysis of the security vulnerabilities commonly found in RESTful APIs.",
    "Could you help me architect a real-time data processing pipeline using Apache Kafka?",
    "What is the most efficient way to handle large-scale image processing in a cloud environment?",
    "I am seeking advice on implementing a robust authentication system using OAuth 2.0 and JWT.",
    "Could you elaborate on the concept of dependency injection and its benefits in software design?",
    "How can I improve the accessibility of my web application according to WCAG standards?",
    "I'm curious about the latest advancements in natural language processing and their practical applications.",
    "What are the pros and cons of using a NoSQL database versus a traditional relational database?",
    "Could you provide a step-by-step tutorial on building a full-stack application with Next.js and Supabase?",
    "How do I configure a CI/CD pipeline using GitHub Actions for a multi-module project?",
    "I would appreciate a detailed explanation of the CAP theorem and its relevance to distributed systems.",
    "What are the key differences between various CSS-in-JS libraries and when should each be used?",
    "Could you demonstrate how to use decorators in Python to implement cross-cutting concerns?",
    "I am looking for a guide on setting up a secure and performant GraphQL server.",
    "What is the best approach for managing secrets and environment variables in a serverless architecture?",
    "Could you explain the inner workings of the Virtual DOM and how it optimizes UI updates?",
    "How can I implement a multi-tenant architecture in a SaaS application efficiently?",
    "I'm interested in the performance characteristics of different sorting algorithms on various data types.",
    "What are the fundamental principles of clean code and how can they be applied in everyday development?",
    "Could you provide a breakdown of the cost and performance trade-offs for different cloud storage options?",
    "How do I implement a custom hook in React for handling complex form state?",
    "I would like to understand the nuances of memory management in C++ and how to avoid memory leaks.",
    "What are the best strategies for load balancing a globally distributed web application?",
    "Could you explain the concept of event sourcing and when it should be utilized in a system?",
    "How can I effectively use Protobuf for inter-service communication in a microservices setup?",
    "I'm seeking recommendations for the best monitoring and logging tools for a production Kubernetes cluster.",
    "Could you provide an overview of the current landscape of mobile app development frameworks?",
    "What are the essential patterns for building resilient and fault-tolerant systems in the cloud?",
    "How do I implement a robust error handling strategy in a Node.js Express application?",
    "I would like to learn about the various types of machine learning models and their specific use cases.",
    "Could you explain the process of performance profiling and optimization for a WebAssembly module?",
    "What are the best practices for documenting a large-scale software project effectively?"
]

normal = [
    "How do I merge two arrays in JavaScript?",
    "Show me a simple way to read a file in Python.",
    "What is the difference between a list and a tuple?",
    "How to change the background color of a div in CSS?",
    "Can you give me a basic SQL query to select all rows from a table?",
    "How do I install a package using npm?",
    "Explain what a function does in programming.",
    "How to center a text in HTML?",
    "What is a variable and how do I use it?",
    "How do I add a new element to a list in Python?",
    "Can you show me how to write a for loop in Java?",
    "How to create a basic React component?",
    "What is the use of the 'git push' command?",
    "How to find the length of a string in C#?",
    "Show me how to use the 'if' statement in C++.",
    "How do I format a date in JavaScript?",
    "What is an API and how does it work?",
    "How to create a simple table in HTML?",
    "How do I commit my changes in Git?",
    "What is a class in object-oriented programming?",
    "How to make an HTTP request in Python?",
    "Show me how to handle an error in JavaScript using try-catch.",
    "How to add a comment in my code?",
    "What is the purpose of the 'head' tag in HTML?",
    "How do I create a new branch in Git?",
    "How to find a value in a dictionary in Python?",
    "Show me a simple example of a switch statement in PHP.",
    "How to redirect a page in HTML?",
    "What is a database and why do we use it?",
    "How do I delete a file using Python?",
    "How to use the 'map' function in JavaScript?",
    "Show me how to create a link in HTML.",
    "How to change the font size of a paragraph in CSS?",
    "What is the difference between '==' and '===' in JavaScript?",
    "How to sort a list in Python?",
    "Show me how to use the 'while' loop in Ruby.",
    "How to create an image tag in HTML?",
    "What is a constant in programming?",
    "How to get the current time in Python?",
    "Show me how to use the 'export' keyword in ES6."
]

tutifuti_english = [
    "bhai, how to make login page in react? simple wala.",
    "me stuck with git error. help karona.",
    "python me list se duplicate kaise nikale? shortcut batao.",
    "mera website slow chal raha hai, optimize kaise karu?",
    "can you explain js callbacks? bahut confusion hai.",
    "how to use groq api? documentation thoda tough hai.",
    "sql me join query kaise likhte hai? example ke sath batao.",
    "mujhe ek code chahiye jo file upload kare server par.",
    "next.js better hai ya plain react? beginner ke liye batao.",
    "how to deploy on vercel? step by step process plzz.",
    "css me grid use karna hai layout ke liye. help me.",
    "variable name kaise decide kare? koi rules hai kya?",
    "mera code crash ho raha hai null pointer se. solve kaise kare?",
    "how to store user session in node js? simple method.",
    "api response thoda late aa raha hai. fast kaise kare?",
    "dark mode feature kaise add kare website me?",
    "mujhe seekhna hai docker. kaha se start karu?",
    "responsive design ke liye media query kaise likhu?",
    "form validation react me kaise karte hai? easy way.",
    "mongodb or postgress, konsa best hai small project ke liye?",
    "tailwind css setup kaise kare vite project me?",
    "how to fetch data from two apis at same time?",
    "mujhe ek weather app banana hai. help karoge?",
    "error handling best practice kya hai express me?",
    "git pull aur fetch me difference kya hai exactly?",
    "local storage me data kaise save kare permanently?",
    "jwt token expiry kaise check kare frontend me?",
    "mujhe ek simple portfolio website ka template chahiye.",
    "how to use environment variables in python safely?",
    "mera component re-render ho raha hai baar baar. stop kaise karu?",
    "typescript me interface aur type me kya fark hai?",
    "django me admin panel customize kaise kare?",
    "how to integrate payment gateway like stripe?",
    "muje unit testing sikhna hai jest ke saath.",
    "how to handle large files in node stream?",
    "website me dynamic routing kaise implement kare?",
    "seo ke liye meta tags kaise set kare automatically?",
    "mujhe ek bot banana hai discord ke liye python me.",
    "firebase setup for push notifications inside react native.",
    "how to use chatgpt api to generate code?"
]

mistakes_errors = [
    "hwo to maked a flis in pythen?",
    "i want loging page cod for webiste",
    "can u hilp me with ssql join querys eror",
    "js mien array ko sort kasie karein?",
    "how too instal nodejs on windos machine",
    "me facing prblm wth git push cmd",
    "plz hlp to fixes ths bug in my code",
    "hwo to center a div usng flex box?",
    "variable nt defined eror in my script",
    "how too use fetch api for get data?",
    "i ned code for emial validtion in react",
    "can u xplain what is redux in shrt?",
    "how to maked resposive nav bar?",
    "sql table me data insert nai ho rha help",
    "hwo to delte a row from database?",
    "python dict mien value search krna h",
    "how to use async await in javascripts?",
    "i want to lern coding from scratch",
    "how to install pip on linux terminal?",
    "cod for simple calculator in c language",
    "how too upload image in firebases?",
    "me stuck on npm install error help",
    "hwo to change password in auth system",
    "can u show me for loop in pythn?",
    "how too used media query in css file?",
    "i want to makes a tictactoe game",
    "javascript function not wirking properly",
    "how to deploy site on github pages?",
    "sql query select frrom table name is wrong",
    "hwo to used dotenv file in node app?",
    "i ned help wth bootstrap cdn link",
    "how to add favicon to html page?",
    "me want to learn machine larning",
    "hwo to makes a crud app in php?",
    "error in python list index out of range",
    "how too used useeffect hook in react?",
    "i want code for responsive footer",
    "hwo to connect nodejs with mongodb?",
    "can u show me how too use docker?",
    "how to create a user profile page?"
]

# Map categories to labels
data = []
for text in fluent_english:
    data.append({"text": text, "label": "fluent"})
for text in normal:
    data.append({"text": text, "label": "normal"})
for text in tutifuti_english:
    data.append({"text": text, "label": "hinglish"}) # or 'tutifuti'
for text in mistakes_errors:
    data.append({"text": text, "label": "error_prone"})

dataset_path = Path(r"f:\New folder (3)\quickvibeai-datasets\datasets.0.0.1.jsonl")
with open(dataset_path, "w", encoding="utf-8") as f:
    for entry in data:
        f.write(json.dumps(entry) + "\n")

# Version Manifest
version_data = {
    "version": "0.0.1",
    "compatibility": {
        "0.1.1": "0.0.1"
    },
    "entries": len(data),
    "released": "2026-04-13"
}

version_path = Path(r"f:\New folder (3)\quickvibeai-datasets\version.json")
with open(version_path, "w", encoding="utf-8") as f:
    json.dump(version_data, f, indent=2)

print(f"Generated {len(data)} entries.")
print(f"Dataset: {dataset_path}")
print(f"Version: {version_path}")
