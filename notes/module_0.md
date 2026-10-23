# I setted up ollama, pulled llama3.2:3b model, ran it. Configured claude and open AI API keys, and ran a basic client code to post a message and get a response which had the following structure (response_text, input_tokens, output_tokens, latency/time_taken)


- In the lab_utils/clients file, I define 3 functions to interact with the different models. When posting, 2 things are surely needed -> model, and messages (which is an array type)

    - So if i pass multiple messages what I expect in resposne?
        - When I passed 2 user role messgaes, Open AI seemed to be ignoring one at times, when the content couldn't be linked, and when I passed 2 questions that can be linked it answered in better

    - There are different roles that I can pass - user, system(content/system instrcuitons), assistnat, and more. i willl explore on it


- Open AI API response
    - ``` ChatCompletion(id='chatcmpl-Ec0XOfYhxhcuzE0FZH9HZUMuqWcW6', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='A token is a small unit of text—suchas a word, part of a word, or punctuation mark—that an LLM processes and generates.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1792727238, model='gpt-6-luna', object='chat.completion', metadata=None, moderation=None, service_tier='default', system_fingerprint=None, usage=CompletionUsage(completion_tokens=61, prompt_tokens=22, total_tokens=83, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=22, rejected_prediction_tokens=0, text_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cache_write_tokens=0, cached_tokens=0, image_tokens=None, text_tokens=None))) ```
- llama API response
    - ``` model='llama3.2:3b' created_at='2026-10-23T03:47:33.4992688Z' done=True done_reason='stop' total_duration=12241768900 load_duration=6147830900 prompt_eval_count=41 prompt_eval_duration=738765000 eval_count=50 eval_duration=5342754000 message=Message(role='assistant', content='In the context of Large Language Models (LLMs), a token refers to a discrete unit of text, such as a word, character, or subword, that is used as the basic building block for input, output, and model processing.', thinking=None, images=None, tool_name=None, tool_calls=None) logprobs=None ```

- [How Github manages multiple local accounts?](https://medium.com/expedia-group-tech/how-to-handle-multiple-git-accounts-385afe430d5a)
    - GPG Signing keys, when commit using them and making gpgsign=true, others cannot use your identity to push commits. We make this by enabling branch protection. If the commits are signed - github shows verfied. By default web UI are already verified ones. 
    - There is `git config --local --list --show-origin`
    - `git config --system --list --show-origin`
    - `git config --global --list --show-origin`

