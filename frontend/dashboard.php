<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RECOR Frontend</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <h1>RECOR Requests</h1>
    
    <h2>Upload Files</h2>
    <form id="upload-form" action="http://127.0.0.1:8000/uploadfiles/" method="post" enctype="multipart/form-data">
        <input type="file" id="file1" name="file1" required>
        <input type="file" id="file2" name="file2" required>
        <input type="file" id="file3" name="file3" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Search User</h2>
    <form id="user-form">
        <input type="text" id="matricule" placeholder="Matricule" required>
        <button type="submit">Search</button>
        
    </form>
    <form id="user-form">
    <input type="text" id="matricule" placeholder="Matricule" required>
    <input type="text" id="telephone" name="telephone" required>
    <button type="submit">Update Telephone</button>
    </form>
    <pre id="user-info"></pre>

    <script src="app.js"></script>
    <script>
        $(document).ready(function () {
            $('#update-telephone-form').on('submit', function (e) {
                e.preventDefault();

                var formData = new FormData(this);

                $.ajax({
                    url: 'http://127.0.0.1:8000/user/' + $('#matricule').val(),
                    type: 'PUT',
                    data: formData,
                    contentType: false,
                    processData: false,
                    success: function (response) {
                        alert('Telephone number updated successfully');
                    },
                    error: function (jqXHR) {
                        alert('Error updating telephone number: ' + jqXHR.responseJSON.detail);
                    }
                });
            });
        });
    </script>
</body>
</html>
