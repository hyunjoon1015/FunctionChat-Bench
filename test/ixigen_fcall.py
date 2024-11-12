import requests
import json

def make_message(system_prompt, user_prompt):
    message = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
    message += system_prompt
    message += "\n<|start_header_id|>user<|end_header_id|>\n"
    message += user_prompt
    message += "<|start_header_id|>assistant<|end_header_id|>\n\n"
    return message

def main():
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "stream": False,
        "temperature": 0.0,
        "top_p": 0.95,
        "repetition_penalty": 1,
        "max_tokens": 4096
    }

    system_prompt = """
    Answer the following questions as best you can. You have access to the following tools:
    - get_today : 오늘 날짜를 알려줍니다. parameters : {}
    - get_path : 출발지와 목적지를 주면 최단 경로를 검색해줍니다. parameters : {"src": "출발지", "dst": "목적지"}
    - get_local : 주어진 장소의 위도/경도 좌표를 줍니다. parameters : {"local": "장소"}
    Answer should be following format:
    {"tool_name": selected tool name to use, "parameters": generated arguments to use selected tool.}
    """
    user_prompt = "마곡사옥에서 용산사옥 가는 길을 알려줘."

    message = make_message(system_prompt, user_prompt)
    request_message = {
        "text_input": message,
        "parameters": params,
        "exclude_input_in_output": True,
        "tr_id": "test_tr_id",
        "pjt_id": "test_pjt_id"
    }

    response = requests.post(
        "https://stvllm-ns-17256059576982515.mng.ip.violet.uplus.co.kr/v2/models/vllm/generate",
        headers=headers,
        json=request_message
    )
    print(json.loads(response.text))

if __name__ == "__main__":
    main()