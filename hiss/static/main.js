$(document).ready(function() {
    const optionalQuestionsNode = 
        `<hr/>
        <h6 style="color:#4286f3; padding: 1em 0em 1em 0em;">
            The following questions are optional. Scroll down to submit your application, or continue to help us improve the event!
        </h6>`;
    // Insert header after shirt_size question.
    $("#id_datascience_experience").parent().append(optionalQuestionsNode);

    // Insert hr above agree checkboxes
    $("#id_agree_to_mlh_policies").parent().prepend("<hr/>");

    const linksHeaderNode = `<h6 style="color: #000; padding: 2em 0em 1em 0em;">Do you have any of the following links to give us?</h6>`;
    // Insert header after last_name question.
    $("#id_last_name").parent().append(linksHeaderNode);

    const indentedInputClass = "indented-input";
    const linkInputIds = ["id_github_link", "id_linkedin_link", "id_personal_website_link", "id_instagram_link", "id_devpost_link", "id_transport_needed", "id_travel_reimbursement", "id_dietary_restrictions", "id_additional_accommodations", "id_physical_location_other"];
    linkInputIds.forEach(id => $(`#${id}`).parent().addClass(indentedInputClass));

    if (!$('#id_race input[value="O"]')[0].checked) {
        $('#id_race_other').parent().hide();
    }
    $('#id_race input[value="O"]').click(function() {
        if ($('#id_race input[value="O"]')[0].checked){
            $('#id_race_other').parent().show();
        }
        else{
            $('#id_race_other').parent().hide();
        }
    });

    if ($('#id_gender').val() !== "X"){
        $('#id_gender_other').parent().hide();
    }
    $('#id_gender').on('change', function(){
         let selection = $('#id_gender').val();
         if (selection === "X"){
            $('#id_gender_other').parent().show();
         }
         else{
             $('#id_gender_other').parent().hide();
         }
    });

    if ($('#id_school option:selected').text() !== "Other"){
        $('#id_school_other').parent().hide();
    }
    $('#id_school').on('change', function(){
         let selection = $('#id_school option:selected').text();
         if (selection === "Other"){
            $('#id_school_other').parent().show();
         }
         else{
             $('#id_school_other').parent().hide();
         }
    });

    const inPersonQuestions = [
        "#id_transport_needed",
        "#id_travel_reimbursement",
        "#id_dietary_restrictions",
        "#id_additional_accommodations"
    ]

    inPersonQuestions.forEach(id => $(id).parent().hide());

    $('#id_location_preference').on('change', function(){
        let selection = $('#id_location_preference option:selected').val();
        if (selection === "prefers_in_person"){
            console.log("show")
            inPersonQuestions.forEach(id => $(id).parent().show())
        }
        else{
            console.log("hide")
            inPersonQuestions.forEach(id => $(id).parent().hide())
        }
    });

    if($("#id_interesting_industries").val().includes("other")) {
        $("#id_industries_other").parent().show();
    } else {
        $("#id_industries_other").parent().hide();
    }
    $('#id_interesting_industries').on('change', () => {
        if($("#id_interesting_industries").val().includes("other")) {
            $("#id_industries_other").parent().show();
        } else {
            $("#id_industries_other").parent().hide();
        }
    });


    if($("#id_physical_location").val() == "other") {
        $("#id_physical_location_other").parent().show();
    } else {
        $("#id_physical_location_other").parent().hide();
    }
    $('#id_physical_location').on('change', () => {
        if($("#id_physical_location").val() == "other") {
            $("#id_physical_location_other").parent().show();
        } else {
            $("#id_physical_location_other").parent().hide();
        }
    });

    // Check for any django-based validation errors and show alert near submit button.
    if($(".errorlist").length > 0) {
        $(".form-incomplete-alert").show();
    } else {
        $(".form-incomplete-alert").hide();
    }

    // Custom styling for multi-select inputs.
    // Reference: https://select2.org/getting-started/basic-usage.
    $('#id_majors').select2();
    $('#id_minors').select2();
    $('#id_technology_experience').select2();
    $('#id_interesting_industries').select2();
})