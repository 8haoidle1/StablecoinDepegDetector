# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

import json
import typing


class StablecoinDepegDetector(gl.Contract):
    has_scanned: bool
    depeg_status: str
    most_at_risk: str
    analysis: str
    param: str

    def __init__(self, param: str):
        self.has_scanned = False
        self.depeg_status = "ALL_STABLE"
        self.most_at_risk = "none"
        self.analysis = "Awaiting scan"
        self.param = param

    @gl.public.write
    def check_depeg(self) -> typing.Any:

        if self.has_scanned:
            return "Already scanned"

        def nondet() -> str:
            fng = gl.nondet.web.render("https://alternative.me/crypto/fear-and-greed-index/", mode="text")
            print(fng)

            task = f"""You are a stablecoin risk analyst. Based on market fear level, assess stablecoin depeg risk.
            Here is current crypto market data:
            {fng[:1500]}

            Respond with the following JSON format:
            {{
                "depeg_status": str,
                "most_at_risk": str,
                "deviation_pct": str,
                "summary": str
            }}
            depeg_status: one of ALL_STABLE, MINOR_DEVIATION, WARNING, CRITICAL_DEPEG.
            most_at_risk: stablecoin most likely to depeg in current conditions.
            deviation_pct: estimated deviation percentage as string.
            summary: one sentence about stablecoin stability.
            It is mandatory that you respond only using the JSON format above,
            nothing else. Don't include any other words or characters,
            your output must be only JSON without any formatting prefix or suffix.
            This result should be perfectly parsable by a JSON parser without errors.
            """
            result = gl.nondet.exec_prompt(task).replace("```json", "").replace("```", "")
            print(result)
            return json.dumps(json.loads(result), sort_keys=True)

        result_json = json.loads(gl.eq_principle.strict_eq(nondet))

        self.has_scanned = True
        self.depeg_status = result_json["depeg_status"]
        self.most_at_risk = result_json["most_at_risk"]
        self.analysis = result_json["summary"]

        return result_json
