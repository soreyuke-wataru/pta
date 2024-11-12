 // 申請日の入力フィールドを同期させる
document.addEventListener('DOMContentLoaded', function() {
    const applicationDateA = document.getElementById('application_date_a');
    const nationalStageDate = document.getElementById('national_stage_date');
    const applicationOrNationalStageDate = document.getElementById('application_or_national_stage_date');
    const patentIssuanceDateA = document.getElementById('patent_issuance_date_a');
    const patentIssuanceDateB = document.getElementById('patent_issuance_date_b');
    
    applicationDateA.addEventListener('change', function(e) {
        applicationOrNationalStageDate.value = e.target.value;
    });
    
    nationalStageDate.addEventListener('change', function(e) {
        applicationOrNationalStageDate.value = e.target.value;
    });

    patentIssuanceDateA.addEventListener('change', function(e) {
        patentIssuanceDateB.value = e.target.value;
    });
    
    patentIssuanceDateB.addEventListener('change', function(e) {
        patentIssuanceDateA.value = e.target.value;
    });
});

async function calculateTotalExcess() {

            const applicationDateA = document.getElementById("application_date_a").value;
            const notificationToApplicationDate = document.getElementById("notification_to_application_date").value;
            const nationalStageDate = document.getElementById("national_stage_date").value;
            const notificationToNationalStageDate = document.getElementById("notification_to_national_stage_date").value;
            const replyUnder132Date = document.getElementById("reply_under_132_date").value;
            const respondToReplyDate = document.getElementById("respond_to_reply_date").value;
            const appealUnder134Date = document.getElementById("appeal_under_134_date").value;
            const respondToAppealDate = document.getElementById("respond_to_appeal_date").value;
            const patentTrialDecisionDate = document.getElementById("Patent_Trial_decision_date").value;
            const respondToPatentTrialDecisionDate = document.getElementById("respond_to_PTdecision_date").value;
            const appealBoardDecisionDate = document.getElementById("Appeal_Board_decision_date").value;
            const respondToAppealBoardDecisionDate = document.getElementById("respond_to_ABdecision_date").value;
            const federalCourtDecisionDate = document.getElementById("Federal_Court_decision_date").value;
            const respondToFederalCourtDecisionDate = document.getElementById("respond_to_FCdecision_date").value;
            const issueFeePaidDate = document.getElementById("issue_fee_paid_date").value;
            const patentIssuanceDateA = document.getElementById("patent_issuance_date_a").value;
            const applicationOrNationalStageDate = document.getElementById("application_or_national_stage_date").value;
            const patentIssuanceDateB = document.getElementById("patent_issuance_date_b").value;
            const delay135a = parseInt(document.getElementById('delay_135a').value) || 0;
            const delay181 = parseInt(document.getElementById('delay_181').value) || 0;
            const delayReview = parseInt(document.getElementById('delay_review').value) || 0;
            const firstOfficeResponseDate = document.getElementById("first_office_response_date").value;
            const firstApplicantResponseDate = document.getElementById("first_applicant_response_date").value;
            const secondOfficeResponseDate = document.getElementById("second_office_response_date").value;
            const secondApplicantResponseDate = document.getElementById("second_applicant_response_date").value;
            const thirdOfficeResponseDate = document.getElementById("third_office_response_date").value;
            const thirdApplicantResponseDate = document.getElementById("third_applicant_response_date").value;
        
            try {
            // 日付をPythonに送信
                const response14 = await fetch("/calculate_excess_14months", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        application_date_a: applicationDateA,
                        notification_to_application_date: notificationToApplicationDate, 
                        national_stage_date: nationalStageDate, 
                        notification_to_national_stage_date: notificationToNationalStageDate 
                    })
                });
                const data14 = await response14.json();
                const excess14 = data14.excess_duration || 0;

                const response4 = await fetch("/calculate_excess_4months", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        reply_under_132_date: replyUnder132Date, 
                        respond_to_reply_date: respondToReplyDate, 
                        appeal_under_134_date: appealUnder134Date, 
                        respond_to_appeal_date: respondToAppealDate, 
                        patent_trial_decision_date: patentTrialDecisionDate, 
                        respond_to_patent_trial_decision_date: respondToPatentTrialDecisionDate, 
                        appeal_board_decision_date: appealBoardDecisionDate, 
                        respond_to_appeal_board_decision_date: respondToAppealBoardDecisionDate, 
                        federal_court_decision_date: federalCourtDecisionDate, 
                        respond_to_federal_court_decision_date: respondToFederalCourtDecisionDate, 
                        issue_fee_paid_date: issueFeePaidDate, 
                        patent_issuance_date_a: patentIssuanceDateA, 
                        application_or_national_stage_date: applicationOrNationalStageDate,
                        patent_issuance_date_b: patentIssuanceDateB 
                    })
                });
                const data4 = await response4.json();
                const excess4 = data4.excess_duration || 0;

                const response36 = await fetch("/calculate_excess_36months", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ application_or_national_stage_date: applicationOrNationalStageDate, patent_issuance_date_b: patentIssuanceDateB })
                });
                const data36 = await response36.json();
                const excess36 = data36.excess_duration || 0;

                const responseDelay = await fetch("/calculate_delay", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ delay_135a: delay135a, delay_181: delay181, delay_review: delayReview })
                });
                const dataDelay = await responseDelay.json();
                const totalDelay = dataDelay.total_delay || 0;

                const finalExcessDays = excess14 + excess4 + excess36 + totalDelay;
                
                const responseOverlapped14  = await fetch("/calculate_overlapped_duration_14months", {  
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        application_date_a: applicationDateA, 
                        notification_to_application_date: notificationToApplicationDate, 
                        national_stage_date: nationalStageDate, 
                        notification_to_national_stage_date: notificationToNationalStageDate,
                        application_or_national_stage_date: applicationOrNationalStageDate,
                        patent_issuance_date_b: patentIssuanceDateB 
                    })
                });
                const dataOverlapped14 = await responseOverlapped14.json();
                const totalOverlapped14 = dataOverlapped14.overlapped_duration || 0;

                const responseOverlapped4 = await fetch("/calculate_overlapped_duration_4months", {  
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        reply_under_132_date: replyUnder132Date, 
                        respond_to_reply_date: respondToReplyDate, 
                        appeal_under_134_date: appealUnder134Date, 
                        respond_to_appeal_date: respondToAppealDate,
                        patent_trial_decision_date: patentTrialDecisionDate, 
                        respond_to_patent_trial_decision_date: respondToPatentTrialDecisionDate,
                        appeal_board_decision_date: appealBoardDecisionDate, 
                        respond_to_appeal_board_decision_date: respondToAppealBoardDecisionDate,
                        federal_court_decision_date: federalCourtDecisionDate, 
                        respond_to_federal_court_decision_date: respondToFederalCourtDecisionDate,
                        issue_fee_paid_date: issueFeePaidDate, 
                        patent_issuance_date_a: patentIssuanceDateA, 
                        application_or_national_stage_date: applicationOrNationalStageDate,
                        patent_issuance_date_b: patentIssuanceDateB 
                    })
                });
                const dataOverlapped4 = await responseOverlapped4.json();
                const totalOverlapped4 = dataOverlapped4.overlapped_duration || 0;

                const responseOverlapped3 = await fetch("/calculate_excess_3months", {  
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ 
                        first_office_response_date: firstOfficeResponseDate, 
                        first_applicant_response_date: firstApplicantResponseDate, 
                        second_office_response_date: secondOfficeResponseDate, 
                        second_applicant_response_date: secondApplicantResponseDate, 
                        third_office_response_date: thirdOfficeResponseDate, 
                        third_applicant_response_date: thirdApplicantResponseDate 
                    })
                });
                const dataOverlapped3 = await responseOverlapped3.json();
                const totalOverlapped3 = dataOverlapped3.excess_duration || 0;
                const adjustedExcessDays = Math.max((finalExcessDays - totalOverlapped14 - totalOverlapped4 - totalOverlapped3), 0);
                // 結果を表示
                document.getElementById("result").innerText = "超過日数: " + adjustedExcessDays;
            } catch (error) {
                console.error("エラー:", error);
                document.getElementById("result").innerText = "エラーが発生しました。";
            }
        }