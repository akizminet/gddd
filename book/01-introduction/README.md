# Introduction

What is Generative DDD? This chapter explores the vision and goals of our methodology.

## A Running Example: Ethan's AI-Powered GTD App

To ground these abstract Domain-Driven Design concepts into something practical, we will follow a single, evolving example throughout this book. 

Meet **Ethan**. Ethan is a solo entrepreneur and developer. Like many of us, he suffers from digital information overload. He has ideas scattered across GitHub issues, Telegram messages, emails, and dozens of open browser tabs. 

Ethan decides to build an application inspired by the **Getting Things Done (GTD)** methodology. However, unlike standard TODO lists (which require manual entry), Ethan's vision is a **Zero-Friction AI-GTD App**.

The defining feature—the "Core Domain" where the business magic happens—is an AI Auto-Capture Engine. This engine runs in the background, continuously analyzing Ethan's digital footprint (reading Telegram chats, monitoring GitHub assignments, scanning emails) and using a Large Language Model to automatically extract actionable tasks and route them into his GTD Inbox.

### Why this Example?
This hypothetical application is perfect for learning DDD because it possesses real domain complexity:
1.  **Core Domain:** The AI Auto-Capture Engine (Intelligent parsing, deduplication, and routing).
2.  **Supporting Domains:** Integrations and Connectors (The infrastructure communicating with the GitHub API, Telegram bots, and Gmail).
3.  **Generic Domains:** Standard Task Management (The lists themselves: Next Actions, Waiting For, Projects, Someday/Maybe).

Throughout Chapter 2, we will watch Ethan attempt to model this complex system using the *Traditional DDD Starter Process*—and experience the friction of doing it alone. Then, in the subsequent chapters, we will observe how Ethan accelerates this same process using **Generative DDD**.
