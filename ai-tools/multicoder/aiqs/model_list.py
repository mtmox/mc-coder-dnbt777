
# OpenRouter models with provider prefixes
openrouter_models = [
    # OpenAI models
    "openai/gpt-5",
    "openai/gpt-4.1-mini",
    "openai/gpt-5-codex",
    "openai/gpt-5-nano",

    # Anthropic models
    "anthropic/claude-sonnet-4",
    "anthropic/claude-opus-4",
    "anthropic/claude-opus-4.1",
    "anthropic/claude-sonnet-4.5",
    
    # Google models
    "google/gemini-2.5-flash-lite",
    "google/gemini-2.5-flash",
    "google/gemini-2.5-pro",
    
    # Deepseek models
    "deepseek/deepseek-v3.2-exp",
    "deepseek/deepseek-v3.1-terminus",
    "deepseek/deepseek-chat-v3.1:free",

    # Grok models
    "x-ai/grok-4-fast:free",
    "x-ai/grok-4-fast",
    "x-ai/grok-code-fast-1",
    "x-ai/grok-4",

    # Qwen models
    "qwen/qwen3-coder",

    # Other models
    "z-ai/glm-4.6",
    "moonshotai/kimi-k2-0905",
    "moonshotai/kimi-k2"
]

# Model pricing information for cost tracking
model_pricing = {
    "openai/gpt-5": {
        "input": 1.25,  # per 1 million tokens
        "output": 10.0,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "openai/gpt-4.1-mini": {
        "input": 0.4,  # per 1 million tokens
        "output": 1.6,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "openai/gpt-5-codex": {
        "input": 1.25,  # per 1 million tokens
        "output": 10.0,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "openai/gpt-5-nano": {
        "input": 0.05,  # per 1 million tokens
        "output": 0.4,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "anthropic/claude-sonnet-4": {
        "input": 3.0,  # per 1 million tokens
        "output": 15.000001,   # per 1 million tokens
        "image": 0.0048,  # per image
        "request": 0.0,  # per request
    },
    "anthropic/claude-opus-4": {
        "input": 15.000001,  # per 1 million tokens
        "output": 75.0,   # per 1 million tokens
        "image": 0.024,  # per image
        "request": 0.0,  # per request
    },
    "anthropic/claude-opus-4.1": {
        "input": 15.000001,  # per 1 million tokens
        "output": 75.0,   # per 1 million tokens
        "image": 0.024,  # per image
        "request": 0.0,  # per request
    },
    "anthropic/claude-sonnet-4.5": {
        "input": 3.0,  # per 1 million tokens
        "output": 15.000001,   # per 1 million tokens
        "image": 0.0048,  # per image
        "request": 0.0,  # per request
    },
    "google/gemini-2.5-flash-lite": {
        "input": 0.1,  # per 1 million tokens
        "output": 0.4,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "google/gemini-2.5-flash": {
        "input": 0.3,  # per 1 million tokens
        "output": 2.5,   # per 1 million tokens
        "image": 0.001238,  # per image
        "request": 0.0,  # per request
    },
    "google/gemini-2.5-pro": {
        "input": 1.25,  # per 1 million tokens
        "output": 10.0,   # per 1 million tokens
        "image": 0.00516,  # per image
        "request": 0.0,  # per request
    },
    "deepseek/deepseek-v3.2-exp": {
        "input": 0.27,  # per 1 million tokens
        "output": 0.4,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "deepseek/deepseek-v3.1-terminus": {
        "input": 0.23,  # per 1 million tokens
        "output": 0.9,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "deepseek/deepseek-chat-v3.1:free": {
        "input": 0.0,  # per 1 million tokens
        "output": 0.0,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "x-ai/grok-4-fast:free": {
        "input": 0.0,  # per 1 million tokens
        "output": 0.0,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "x-ai/grok-4-fast": {
        "input": 0.2,  # per 1 million tokens
        "output": 0.5,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "x-ai/grok-code-fast-1": {
        "input": 0.2,  # per 1 million tokens
        "output": 1.5,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "x-ai/grok-4": {
        "input": 3.0,  # per 1 million tokens
        "output": 15.000001,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "qwen/qwen3-coder": {
        "input": 0.22,  # per 1 million tokens
        "output": 0.95,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "z-ai/glm-4.6": {
        "input": 0.5,  # per 1 million tokens
        "output": 1.75,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "moonshotai/kimi-k2-0905": {
        "input": 0.4,  # per 1 million tokens
        "output": 2.0,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
    "moonshotai/kimi-k2": {
        "input": 0.14,  # per 1 million tokens
        "output": 2.49,   # per 1 million tokens
        "image": 0.0,  # per image
        "request": 0.0,  # per request
    },
}
