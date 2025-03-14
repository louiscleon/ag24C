from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Charge la configuration LLM depuis le fichier OAI_CONFIG_LIST
llm_config = {
    "config_list": config_list_from_json(env_or_file="OAI_CONFIG_LIST")
}

# Crée l'agent assistant
assistant = AssistantAgent("assistant", llm_config=llm_config)

# Crée l'agent qui simule l'interaction utilisateur
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False})

# Lancer la conversation entre les agents
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")