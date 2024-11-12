from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# 日付フォーマットの定義
DATE_FORMAT = "%Y-%m-%d"

def calculate_excess_duration(date_a_str, date_b_str, months):
    date_a = datetime.strptime(date_a_str, DATE_FORMAT)
    date_b = datetime.strptime(date_b_str, DATE_FORMAT)
    threshold_date = date_a + relativedelta(months=months)  
    excess_duration = max(0, (date_b - threshold_date).days)
    return excess_duration

def adjust_excess_duration(date_a_str, date_b_str, date_c_str, date_d_str, months):
    date_a = datetime.strptime(date_a_str, DATE_FORMAT)
    date_b = datetime.strptime(date_b_str, DATE_FORMAT)
    date_c = datetime.strptime(date_c_str, DATE_FORMAT)
    date_d = datetime.strptime(date_d_str, DATE_FORMAT)
    threshold_start_date = date_a + relativedelta(months=months)
    threshold_end_date = date_c + relativedelta(months=36)
    overlapped_duration = max((min(date_b, date_d) - max(threshold_start_date, threshold_end_date)).days, 0)
    return overlapped_duration

@app.route("/calculate_excess_14months", methods=["POST"])
def calculate_14months():
    data = request.get_json()
    total_excess_duration = 0
    application_date_a = data.get("application_date_a")
    notification_to_application_date = data.get("notification_to_application_date")
    national_stage_date = data.get("national_stage_date")
    notification_to_national_stage_date = data.get("notification_to_national_stage_date")

    if application_date_a and notification_to_application_date:
        excess_duration_application = calculate_excess_duration(application_date_a, notification_to_application_date, 14)
        total_excess_duration += excess_duration_application
    if national_stage_date and notification_to_national_stage_date:
        excess_duration_national_stage = calculate_excess_duration(national_stage_date, notification_to_national_stage_date, 14)
        total_excess_duration += excess_duration_national_stage
    return jsonify({"excess_duration": total_excess_duration})

    
@app.route("/calculate_excess_4months", methods=["POST"])
def calculate_4months():
    data = request.get_json()
    total_excess_duration = 0
    reply_under_132_date = data.get("reply_under_132_date")
    respond_to_reply_date = data.get("respond_to_reply_date")
    appeal_under_134_date = data.get("appeal_under_134_date")
    respond_to_appeal_date = data.get("respond_to_appeal_date")
    patent_trial_decision_date = data.get("patent_trial_decision_date")
    respond_to_patent_trial_decision_date = data.get("respond_to_patent_trial_decision_date")
    appeal_board_decision_date = data.get("appeal_board_decision_date")
    respond_to_appeal_board_decision_date = data.get("respond_to_appeal_board_decision_date")
    federal_court_decision_date = data.get("federal_court_decision_date")
    respond_to_federal_court_decision_date = data.get("respond_to_federal_court_decision_date")
    issue_fee_paid_date = data.get("issue_fee_paid_date")
    patent_issuance_date_a = data.get("patent_issuance_date_a")
    
    if reply_under_132_date and respond_to_reply_date:
        excess_duration_reply = calculate_excess_duration(reply_under_132_date, respond_to_reply_date, 4)
        total_excess_duration += excess_duration_reply
    if appeal_under_134_date and respond_to_appeal_date:
        excess_duration_appeal = calculate_excess_duration(appeal_under_134_date, respond_to_appeal_date, 4)
        total_excess_duration += excess_duration_appeal
    if patent_trial_decision_date and respond_to_patent_trial_decision_date:
        excess_duration_patent_trial = calculate_excess_duration(patent_trial_decision_date, respond_to_patent_trial_decision_date, 4)
        total_excess_duration += excess_duration_patent_trial
    if appeal_board_decision_date and respond_to_appeal_board_decision_date:
        excess_duration_appeal_board = calculate_excess_duration(appeal_board_decision_date, respond_to_appeal_board_decision_date, 4)
        total_excess_duration += excess_duration_appeal_board
    if federal_court_decision_date and respond_to_federal_court_decision_date:
        excess_duration_federal_court = calculate_excess_duration(federal_court_decision_date, respond_to_federal_court_decision_date, 4)
        total_excess_duration += excess_duration_federal_court
    if issue_fee_paid_date and patent_issuance_date_a:
        excess_duration_issue_fee = calculate_excess_duration(issue_fee_paid_date, patent_issuance_date_a, 4)
        total_excess_duration += excess_duration_issue_fee
    return jsonify({"excess_duration": total_excess_duration})

@app.route("/calculate_excess_3months", methods=["POST"])
def calculate_3months():
    data = request.get_json()
    total_excess_duration = 0
    first_office_response_date = data.get("first_office_response_date")
    first_applicant_response_date = data.get("first_applicant_response_date")
    second_office_response_date = data.get("second_office_response_date")
    second_applicant_response_date = data.get("second_applicant_response_date")
    third_office_response_date = data.get("third_office_response_date")
    third_applicant_response_date = data.get("third_applicant_response_date")
    if first_office_response_date and first_applicant_response_date:
        excess_duration_first = calculate_excess_duration(first_office_response_date, first_applicant_response_date, 3)
        total_excess_duration += excess_duration_first
    if second_office_response_date and second_applicant_response_date:
        excess_duration_second = calculate_excess_duration(second_office_response_date, second_applicant_response_date, 3)
        total_excess_duration += excess_duration_second
    if third_office_response_date and third_applicant_response_date:
        excess_duration_third = calculate_excess_duration(third_office_response_date, third_applicant_response_date, 3)
        total_excess_duration += excess_duration_third
    return jsonify({"excess_duration": total_excess_duration})

@app.route("/calculate_excess_36months", methods=["POST"])
def calculate_36months():
    data = request.get_json()
    total_excess_duration = 0
    application_or_national_stage_date = data.get("application_or_national_stage_date")
    patent_issuance_date_b = data.get("patent_issuance_date_b")
    
    if application_or_national_stage_date and patent_issuance_date_b:
        excess_duration = calculate_excess_duration(application_or_national_stage_date, patent_issuance_date_b, 36)
        total_excess_duration += excess_duration
    return jsonify({"excess_duration": total_excess_duration})


@app.route("/calculate_delay", methods=["POST"])
def calculate_delay():
    data = request.get_json()
    total_delay = 0
    delay_135a = data.get("delay_135a")
    delay_181 = data.get("delay_181")
    delay_review = data.get("delay_review")
    if delay_135a:
        total_delay += delay_135a
    if delay_181:
        total_delay += delay_181
    if delay_review:
        total_delay += delay_review
    return jsonify({"total_delay": total_delay})

@app.route("/calculate_overlapped_duration_14months", methods=["POST"])
def calculate_overlapped_duration_14months():
    data = request.get_json()
    total_overlapped_duration = 0

    application_date_a = data.get("application_date_a")
    notification_to_application_date = data.get("notification_to_application_date")
    national_stage_date = data.get("national_stage_date")
    notification_to_national_stage_date = data.get("notification_to_national_stage_date")
    application_or_national_stage_date = data.get("application_or_national_stage_date")
    patent_issuance_date_b = data.get("patent_issuance_date_b")
    
    if application_date_a and notification_to_application_date and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(application_date_a, notification_to_application_date, application_or_national_stage_date, patent_issuance_date_b, 14)
    if national_stage_date and notification_to_national_stage_date and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(national_stage_date, notification_to_national_stage_date, application_or_national_stage_date, patent_issuance_date_b, 14)
        
    return jsonify({"overlapped_duration": total_overlapped_duration})

@app.route("/calculate_overlapped_duration_4months", methods=["POST"])
def calculate_overlapped_duration_4months():
    data = request.get_json()  
    total_overlapped_duration = 0
    reply_under_132_date = data.get("reply_under_132_date")
    respond_to_reply_date = data.get("respond_to_reply_date")
    appeal_under_134_date = data.get("appeal_under_134_date")
    respond_to_appeal_date = data.get("respond_to_appeal_date")
    patent_trial_decision_date = data.get("patent_trial_decision_date")
    respond_to_patent_trial_decision_date = data.get("respond_to_patent_trial_decision_date")
    appeal_board_decision_date = data.get("appeal_board_decision_date")
    respond_to_appeal_board_decision_date = data.get("respond_to_appeal_board_decision_date")
    federal_court_decision_date = data.get("federal_court_decision_date")
    respond_to_federal_court_decision_date = data.get("respond_to_federal_court_decision_date")
    issue_fee_paid_date = data.get("issue_fee_paid_date")
    patent_issuance_date_a = data.get("patent_issuance_date_a")
    application_or_national_stage_date = data.get("application_or_national_stage_date")
    patent_issuance_date_b = data.get("patent_issuance_date_b")

    if reply_under_132_date and respond_to_reply_date and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(reply_under_132_date, respond_to_reply_date, application_or_national_stage_date, patent_issuance_date_b, 4)
    if appeal_under_134_date and respond_to_appeal_date and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(appeal_under_134_date, respond_to_appeal_date, application_or_national_stage_date, patent_issuance_date_b, 4)
    if patent_trial_decision_date and respond_to_patent_trial_decision_date and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(patent_trial_decision_date, respond_to_patent_trial_decision_date, application_or_national_stage_date, patent_issuance_date_b, 4)
    if appeal_board_decision_date and respond_to_appeal_board_decision_date and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(appeal_board_decision_date, respond_to_appeal_board_decision_date, application_or_national_stage_date, patent_issuance_date_b, 4)
    if federal_court_decision_date and respond_to_federal_court_decision_date and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(federal_court_decision_date, respond_to_federal_court_decision_date, application_or_national_stage_date, patent_issuance_date_b, 4)
    if issue_fee_paid_date and patent_issuance_date_a and application_or_national_stage_date and patent_issuance_date_b:
        total_overlapped_duration += adjust_excess_duration(issue_fee_paid_date, patent_issuance_date_a, application_or_national_stage_date, patent_issuance_date_b, 4)
    return jsonify({"overlapped_duration": total_overlapped_duration})


# ルートパスへのアクセスでHTMLを提供
@app.route("/")
def index():
    return send_from_directory(".", "pta.html")

# JavaScriptファイルへのアクセスを提供
@app.route("/pta.js")
def serve_js():
    return send_from_directory(".", "pta.js")

if __name__ == "__main__":
    app.run(debug=True)