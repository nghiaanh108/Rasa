# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Action_action_utter_contract_question(Action):

    def name(self) -> Text:
        return "action_utter_contract_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        check_ask_for_time = "F"
        check_salary = "F"
        check_staff = "F"
        check_calculate = "F"
        check_ask_properties_methods = "F"
        check_increase = "F"
        check_ask_for_quantity = "F"
        check_treatment = "F"
        check_ask_yes_no = "F"
        value_date = ""
        value_contract = ""
        check_review = "F"

        mes = "Chưa có câu trả lời hoặc chưa đúng cú pháp câu"
        for e in entities:
            if e['entity'] == "contract":
                value_contract = e['value']
            if e['entity'] == "ask_for_time":
                check_ask_for_time = "T"
            if e['entity'] == "salary":
                check_salary = "T"
            if e['entity'] == "staff":
                check_staff = "T"
            if e['entity'] == "calculate":
                check_calculate = "T"
            if e['entity'] == "ask_properties_methods":
                check_ask_properties_methods = "T"
            if e['entity'] == "increase":
                check_increase = "T"
            if e['entity'] == "ask_for_quantity":
                check_ask_for_quantity = "T"
            if e['entity'] == "treatment":
                check_treatment = "T"
            if e['entity'] == "ask_yes_no":
                check_ask_yes_no = "T"
            if e['entity'] == "date":
                value_date = e['value']
            if e['entity'] == "review":
                check_review = "T"

        lists_TL = ["thử việc"]
        lists_Fr = ["fresher"]
        list_TN = ["thực nghiệm"]
        list_AI = ["aicamp", "ai camp"]
        date_13 = ["tháng 13", "tháng mười ba"]
        if value_contract.lower() in lists_TL and check_ask_for_time == "T" or value_contract.lower() in lists_TL:
            mes = "Hợp đồng thử việc có thời gian 2 tháng."
        if value_contract.lower() in lists_Fr and check_ask_for_time == "T" or value_contract.lower() in lists_Fr:
            mes = "Hợp đồng đào tạo Fresher có thời gian từ 3 đến 3.5 tháng."
        if value_contract.lower() in list_TN and check_ask_for_time == "T" or value_contract.lower() in list_TN:
            mes = "Hợp đồng đào tạo thực nghiệm (on-job-training) kéo dài tối đa 6 tháng."
        if value_contract.lower() in list_AI and check_ask_for_time == "T" or value_contract.lower() in list_AI:
            mes = "Hợp đồng đào tạo AICamp kéo dài tối đa 6 tháng."
        if check_salary == "T" and check_ask_for_time == "T" or check_staff == "T" and check_salary == "T" and check_ask_for_time == "T":
            mes = "Ngày 19 hàng tháng nhân viên sẽ được nhận lương."
        if check_review == "T" and check_ask_for_quantity == "T" and check_salary == "T" or check_review == "T" and check_salary == "T":
            mes = "Một lần trong năm sẽ được review và vào thời gian cuối năm."
        if check_salary == "T" and check_ask_properties_methods == "T" and check_calculate == "T" and value_date.lower() in date_13 or value_date.lower() in date_13 and check_salary == "T" or check_calculate == "T" and value_date.lower() in date_13 and check_salary == "T":
            mes = "Tiền lương tháng 13 được tính bằng lương của tháng 12."
        if check_increase == "T" and check_ask_for_quantity == "T" and check_salary == "T":
            mes = "Định kỳ hằng năm 1 lần."
        if check_calculate == "T" and check_ask_for_quantity == "T" and check_salary == "T" or check_calculate == "T" and check_salary == "T" and value_date.lower() not in date_13:
            mes = "Lương mỗi tháng bằng tiền cướp ngân hàng + tình lương công ty"
        if check_treatment == "T" and check_ask_for_quantity == "T" or check_treatment == "T":
            mes = "Chưa có câu trả lời cho phương thức đãi ngộ nhân viên"
        if check_ask_yes_no == "T" and check_salary == "T" and value_date.lower() == "ngày 19":
            mes = "Đúng rồi!"

        dispatcher.utter_message(text=mes)

        return []


class Action_organizational_structure_question(Action):

    def name(self) -> Text:
        return "action_organizational_structure_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        check_ask_properties_methods = "F"
        check_ask_for_quantity = "F"
        check_ask_people = "F"
        value_position = ""
        value_organization = ""
        check_name = ""
        check_ask_people = "F"
        mes = "Chưa có câu trả lời hoặc chưa đúng ý nghĩa câu"
        for e in entities:
            if e['entity'] == "organization":
                value_organization = e['value']
            if e['entity'] == "position":
                value_position = e['value']
            if e['entity'] == "ask_people":
                check_ask_people = "T"
            if e['entity'] == "ask_for_quantity":
                check_ask_for_quantity = "T"
            if e['entity'] == "ask_properties_methods":
                check_ask_properties_methods = "T"
            if e['entity'] == "name":
                check_name = e['value']
            if e['entity'] == "ask_people":
                check_ask_people = "T"
        lists_Fs = ["fsoft quy nhơn", "fsoft qn", "fpt qn",
                    "fpt quy nhơn", "fpt software qn", "fpt software quy nhơn"]
        lists_TT = ["trung tâm nghiên cứu và ứng dụng trí tuệ nhân tạo quy nhơn",
                    "ttncvudttntqn", "ttnc vả udttntqn", "qai"]
        lists_QAI = ["qai"]
        list_en = ["giám đốc", "chủ", "đứng đầu"]
        if value_organization.lower() in lists_QAI and check_ask_for_quantity == "T":
            mes = "AIA, AIO, COE, AICamp,..."
        if value_organization.lower() in lists_QAI and check_ask_people == "T":
            mes = "AIO: TrongNV5, BUL, AIO: CuongVT1, COE: VinhVDQ, AIC: PhongNX, (team lead tại QNh là khangVNT1,) AICamp là anh Tấn."
        if value_organization.lower() in lists_Fs and value_position in list_en and check_ask_people == "T" or value_organization.lower() in lists_Fs and value_position in list_en:
            mes = "anh Vũ Văn Đông là giám đốc Fsoft Quy Nhơn."
        if value_organization.lower() in lists_TT and value_position in list_en and check_ask_people == "T" or value_organization.lower() in lists_TT and value_position in list_en:
            mes = "anh Vũ Hồng Chiên là Trung tâm Nghiên cứu và Ứng dụng Trí tuệ nhân tạo Quy Nhơn."
        if value_organization.lower() in lists_QAI and check_ask_properties_methods == "T":
            mes = "gồm các bộ phận: AIA, AIO, COE, AICamp"
        if value_organization.lower() in lists_Fs and check_ask_for_quantity == "T":
            mes = "Các bộ phận của Fsoft Quy Nhơn: PID, FID, SEPG.PRO, IT, UTOP, QAI, DPS, GAM, FST, SSC, AF, FWA, ...."
        if check_name.lower() == "vũ văn đông" and check_ask_people == "T":
            mes = "Anh Vũ Văn Đông là giám đốc Fsoft Quy Nhơn"
        if check_name.lower() == "vũ hồng chiên" and check_ask_people == "T":
            mes = "Anh Vũ Hồng Chiên là giám đốc Trung tâm Nghiên cứu và Ứng dụng trí tuệ nhân tạo Quy Nhơn"
        if check_name.lower() == "nguyễn trung trí" and check_ask_people == "T":
            mes = "Anh Nguyễn Trung Trí là PM dự án"
        if check_name.lower() == "mai thành tấn" and check_ask_people == "T":
            mes = "Anh Mai Thành Tấn là quản lý chương trình AICamp"
        if check_name.lower() == "nguyễn văn vinh" and check_ask_people == "T":
            mes = "Anh Nguyễn Văn Vinh là mentor của chương trình AICamp"
        dispatcher.utter_message(text=mes)

        return []


class Action_organizational_structure_question(Action):

    def name(self) -> Text:
        return "action_utter_working_time_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        value_organization = ""
        check_ask_for_time = "F"
        mes = "Chưa có câu trả lời cụ thể cho trường hợp này"
        for e in entities:
            if e['entity'] == "organization":
                value_organization = e['value']
            if e['entity'] == "ask_for_time":
                check_ask_for_time = "T"

        lists_Fs = ["fsoft quy nhơn", "fsoft qn", "trung tâm nghiên cứu và ứng dụng trí tuệ nhân tạo quy nhơn",
                    "ttncvudttntqn", "ttnc vả udttntqn", "qai"]

        if value_organization.lower() in lists_Fs and check_ask_for_time == "T" or value_organization.lower() in lists_Fs:
            mes = "Thời gian làm việc tại "+value_organization + \
                "Bắt đầu lúc 8 giờ và kết thúc lúc 17 giờ, nghỉ trưa từ 12 giờ đến 13 giờ."

        dispatcher.utter_message(text=mes)

        return []


class Action_policy_question(Action):

    def name(self) -> Text:
        return "action_utter_policy_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        value_insurance = ""
        value_location = ""
        check_payment = "F"
        check_ask_for_quantity = "F"
        check_decrease = "F"
        check_ask_properties_methods = "F"
        check_salary = "F"
        check_rules = "F"
        check_important = "F"
        check_union_regime = "F"
        check_union_money = "F"
        check_lunch_support = "F"
        check_ask_yes_no = "F"
        check_work_roaming = "F"
        check_home_buying_support = "F"
        check_calculate = "F"
        check_subsidize = "F"
        check_go_on_bussiness = "F"
        check_family = "F"
        check_staff = "F"
        check_personal_income_tax = "F"
        mes = "Chưa có câu trả lời cụ thể cho trường hợp này"
        for e in entities:
            if e['entity'] == "insurance":
                value_insurance = e['value']
            if e['entity'] == "location":
                value_location = e['value']
            if e['entity'] == "payment":
                check_payment = "T"
            if e['entity'] == "ask_for_quantity":
                check_ask_for_quantity = "T"
            if e['entity'] == "decrease":
                check_decrease = "T"
            if e['entity'] == "ask_properties_methods":
                check_ask_properties_methods = "T"
            if e['entity'] == "salary":
                check_salary = "T"
            if e['entity'] == "rules":
                check_rules = "T"
            if e['entity'] == "important":
                check_important = "T"
            if e['entity'] == "union_regime":
                check_union_regime = "T"
            if e['entity'] == "union_money":
                check_union_money = "T"
            if e['entity'] == "lunch_support":
                check_lunch_support = "T"
            if e['entity'] == "ask_yes_no":
                check_ask_yes_no = "T"
            if e['entity'] == "work_roaming":
                check_work_roaming = "T"
            if e['entity'] == "home_buying_support":
                check_home_buying_support = "T"
            if e['entity'] == "calculate":
                check_calculate = "T"
            if e['entity'] == "subsidize":
                check_subsidize = "T"
            if e['entity'] == "go_on_bussiness":
                check_go_on_bussiness = "T"
            if e['entity'] == "family":
                check_family = "T"
            if e['entity'] == "staff":
                check_staff = "T"
            if e['entity'] == "personal_income_tax":
                check_personal_income_tax = "T"

        lists_BH = ["bảo hiểm", "bảo hiểm y tế",
            "bảo hiểm xã hội", "bảo hiểm thất nghiệp"]
        lists_BHFPT = ["bảo hiểm fpt care", "fpt care"]
        lists_Lo = ["quy nhơn", "qn", "hà nội", "hn"]
        if value_insurance.lower() in lists_BH and check_payment == "T" and check_ask_for_quantity == "T":
            mes = "Bảo hiểm xã hội: công ty đóng 17.5%, nhân viên đóng 8%. Bảo hiểm y tế: công ty đóng 3%, nhân viên đóng 1.5%. Bảo hiểm thất nghiệp: công ty đóng 1%, nhân viên đóng 1%."
        if check_decrease == "T" and check_ask_properties_methods == "T" and check_salary == "T":
            mes = "Nghỉ việc không phép, lộ thông tin của công ty, có hành vi lợi dụng chiếm đoạt tài sản và bị kỹ luật"
        if check_rules == "T" and check_ask_properties_methods == "T" and check_important == "T":
            mes = "Chưa có câu trả lời cho câu hỏi các quy định cần chú ý"
        if check_union_regime == "T" and check_ask_properties_methods == "T":
            mes = "Chưa có câu trả lời cho câu hỏi về các quyền lợi trong chế độ công đoàn"
        if check_union_money == "T" and check_ask_properties_methods == "T":
            mes = "Chưa có câu trả lời cho câu hỏi về cách sử dụng tiền trong chế độ công đoàn"
        if check_lunch_support == "T" and check_ask_yes_no == "T":
            mes = "Không có hỗ trợ cơm trưa cho nhân viên"
        if check_work_roaming == "T" and check_ask_properties_methods == "T" and value_location.lower() in lists_Lo:
            mes = "Hỗ trợ nhà công vụ,..."
        if check_home_buying_support == "T" and check_ask_properties_methods == "T":
            mes = "Chưa có câu trả lời cho câu hỏi về chính sách hỗ trợ mua nhà cho nhân viên"
        if check_calculate == "T" and check_ask_properties_methods == "T" and value_insurance in lists_BHFPT:
            mes = "Chưa có câu trả lời cho câu hỏi về cách tính bảo hiểm FPT Care"
        if check_subsidize == "T" and check_go_on_bussiness == "T" and check_ask_properties_methods == "T":
            mes = "Chưa có câu trả lời cho câu hỏi về trợ cấp công tác cho nhân viên"
        if check_subsidize == "T" and check_family == "T" and check_staff == "T":
            mes = "Chưa có câu trả lời cho câu hỏi về trợ cấp cho gia đình của nhân viên"
        if check_personal_income_tax == "T" and check_ask_properties_methods == "T" or check_personal_income_tax == "T":
            mes = "Cách tính thuế thu nhập đối với thu nhập từ tiền lương, tiền công(hợp đồng lao động lớn hơn 3 tháng) được tính theo công thức sau:" +"\n(1) Thuế thu nhập cá nhân phải nộp = Thu nhập tính thuế x Thuế suất"+"\nTrong đó:"+"\n(2) Thu nhập tính thuế = Thu nhập chịu thuế - Các khoản giảm trừ"+"\nThu nhập chịu thuế được tính như sau:" +"\n(3) Thu nhập chịu thuế = Tổng thu nhập - Các khoản được miễn"
        if check_calculate== "T" and check_salary == "T" and check_personal_income_tax == "T" and check_ask_for_quantity == "T":
            mes = " Người lao động làm việc có tổng thu nhập từ tiền lương, tiền công trên 11 triệu đồng/tháng (nếu không có người phụ thuộc) mới phải nộp thuế thu nhập cá nhân. Nếu có người phụ thuộc thì cộng thêm 4,4 triệu đồng/người."
        dispatcher.utter_message(text=mes)

        return []
