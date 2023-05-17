
# ChatGPT plugins Push2Notion


<br>
If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

Modify the DATA_HOST parameter in `app.py` with your actual domain name, for example:
```
DATA_HOST = "https://<YOUR_REPO>--<YOUR_OWNER>.repl.co"
```
Important: Please use your own HTTPS domain here.

Refer to [domain-verification-and-security](https://platform.openai.com/docs/plugins/production/domain-verification-and-security) for more information.

> Use TLS and HTTPS: All traffic with the plugin (e.g., fetching the ai-plugin.json file, the OpenAPI spec, API calls) must use TLS 1.2 or later on port 443 with a valid public certificate.

You can also modify your contact_email in `/.well-known/ai-plugin.json`.

To run the plugin, enter the following command:

```bash
python app.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

If you are using a VPN or want to run it on a server, I highly recommend trying [replit](https://replit.com/). You can check the project's configuration on replit [gpt-2-notion](https://replit.com/@liompei/gpt-2-notion). You need to do the following:

1. Copy this project from Github to your replit space
2. Modify the `DATA_HOST` parameter in app.py with the HTTPS address of your current project.
3. open Chatgpt Plugin store,Enter the `replit address` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "What is on my todo list" and then try adding something to it as well! 

### How to use Push2Notion

1. Create a Notion integration at [my-integrations](https://www.notion.so/my-integrations) and record your Notion integrations key.

    <div style="width: 70%; margin: 0 auto;">
        <img src="/static/create_integration.png" style="max-width: 100%; height: auto; margin-right: auto">
        <img src="/static/your_integration.png" style="max-width: 100%; height: auto; margin-right: auto">
    </div>

2. Create a database in Notion and link it to the integration. The database has three properties, Name: Type is Title, gpt: Type is Text, and Date: Type is Date
    <div style="width: 70%; margin: 0 auto;">
        <img src="/static/create_database_page.png" style="max-width: 100%; height: auto; margin-right: auto">
        <img src="/static/new_database.png" style="max-width: 100%; height: auto; margin-right: auto">
        <img src="/static/gpt_content.png" style="max-width: 100%; height: auto; margin-right: auto">
        <img src="/static/add_connection.png" style="max-width: 100%; height: auto; margin-right: auto">
   </div>
3. Find the database_id of your page.
    <div style="width: 70%; margin: 0 auto;">
        <img src="/static/copy_link.png" style="max-width: 100%; height: auto; margin-right: auto">
        <img src="/static/database_id_link.png" style="max-width: 100%; height: auto; margin-right: auto">
   </div>
4. During the conversation with GPT, when you need to save the conversation content to Notion, GPT will ask you to provide the integrations and database_id parameters. This operation only needs to be done once.
    <div style="width: 70%; margin: 0 auto;">
        <img src="/static/choose_gpt_plugin.png" style="max-width: 100%; height: auto; margin-right: auto">
        <img src="/static/set_key.png" style="max-width: 100%; height: auto; margin-right: auto">
        <img src="/static/save_notion.png" style="max-width: 100%; height: auto; margin-right: auto">
   </div>
5. OK! From now on, when you say "Save to Notion" to GPT, it will automatically save the content.

## Getting help

If you run into issues or have questions building a plugin, please join [OPENAI Developer community forum](https://community.openai.com/c/chat-plugins/20).

## Link

* [https://openai.com/waitlist/plugins](https://openai.com/waitlist/plugins)
* [https://platform.openai.com/docs/plugins/getting-started/plugin-manifest](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest)
* [https://replit.com/](https://replit.com/)
* [https://replit.com/@liompei/gpt-2-notion](https://replit.com/@liompei/gpt-2-notion)
* [https://gazeonai.com/](https://gazeonai.com/)


