function deleteProject(id) {
    $.ajax({
        url: '/startTime/',
        type: 'POST',
        data: {
            "projectID": id,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }
    });
}