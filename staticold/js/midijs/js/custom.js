function formatDate(date) {
      var hours = date.getHours();
      var minutes = date.getMinutes();
      var ampm = hours >= 12 ? 'pm' : 'am';
      hours = hours % 12;
      hours = hours ? hours : 12; // the hour '0' should be '12'
      minutes = minutes < 10 ? '0' + minutes : minutes;
      var strTime = hours + ':' + minutes + ' ' + ampm;
      return date.getMonth()+1 + "/" + date.getDate() + "/" + date.getFullYear() + "  " + strTime;
}



$(document).ready(function(){


            //on click the class pid is passed in the url
            $(".projectBox").click(function(event) {
                var id =$(this).attr('id');
                var res_id =this.id;
                var res_id = res_id.split("_");
                //window.open('generatedlink.php?inkgen='+$("#linkgen").val());
                window.location = "project_space?pid="+res_id[1];
            });

            $(".projectBox").hover(function() {
                $(this).css('cursor','pointer');
            });

            $("#spk_success_close").on("click", function() {
                $('#modal_default_7').hide();
                //after the hide of pop-up refresh the page to load the forms
                window.location = "create_entity";
            });

            $("#spk_success_closex").on("click", function() {
                $('#modal_default_7').hide();
                //after the hide of pop-up refresh the page to load the forms
                window.location = "create_entity";
            });

            $("#spk_danger_close").on("click", function() {
                $('#modal_default_9').hide();
                //after the hide of pop-up refresh the page to load the forms
                window.location = "create_entity";
            });

            $("#spk_danger_closex").on("click", function() {
                $('#modal_default_9').hide();
                //after the hide of pop-up refresh the page to load the forms
                window.location = "create_entity";
            });


            //Edit Project Form Setting Code
            //From hidden field in the project box fetch all the values
            //Set the fetched values to the form fields
            $(".spk_project_edit").on("click", function() {
                //get the clicked project div id
                //split the id by underscode
                //fetch the prokect key
                var id =$(this).attr('id');
                var res_id =this.id;
                var res_id = res_id.split("_");

                var url=document.getElementById("url_"+res_id[1]).value;
                var name=document.getElementById("name_"+res_id[1]).value;
                var code=document.getElementById("code_"+res_id[1]).value;
                var start_date=document.getElementById("start_date_"+res_id[1]).value;
                var end_date=document.getElementById("end_date_"+res_id[1]).value;
                var fps=document.getElementById("fps_"+res_id[1]).value;
                var resolution=document.getElementById("resolution_"+res_id[1]).value;
                var project_type=document.getElementById("ptype_"+res_id[1]).value;
                var project_path=document.getElementById("prj_path_"+res_id[1]).value;

               $('#editformdet #id_name').val(name);
               $('#editformdet #id_code').val(code);
               $('#editformdet #id_start_date').val(start_date);
               $('#editformdet #id_end_date').val(end_date);
               //$("#editformdet #id_fps select").val("val2");
               //alert(fps);
               $('#editformdet #id_fps').val(fps);
               $('#editformdet #id_resolution').val(resolution);
               $('#editformdet #id_project_type').val(project_type);
               $('#editformdet #id_project_path').val(project_path);
               $('#editformdet #id_url').val(url);

               $('#editformdet #id_code').prop("readonly",true);
               $('#editformdet #id_url').prop("readonly",true);
               $('#editformdet #id_project_path').prop("readonly",true);

               //$('#editformdet #id_fps select').val(fps);
               //$('#editformdet #id_resolution select').val(resolution);
            });

            //Delete project

            $(".spk_project_delete").on("click", function(){
                //get the clicked project div id
                //split the id by underscode
                //fetch the prokect key
                var id =$(this).attr('id');
                var res_id =this.id;
                var res_id = res_id.split("_");

                //fetch values from the hidden field
                var url=document.getElementById("url_"+res_id[1]).value;
                var name=document.getElementById("name_"+res_id[1]).value;
                var code=document.getElementById("code_"+res_id[1]).value;

               //fill the model box field values
               $('#deleteprojectform #name').val(name);
               $('#deleteprojectform #code').val(code);
               $('#deleteprojectform #url').val(url);
            });


            $("#pc_prj_delete_btn").on("click", function() {
                var out = $('#deleteprojectform #url').value;
                console.log(out);
                alert(out);
                //window.location = "api/project/" ;
            });

});
