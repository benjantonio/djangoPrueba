
$( document ).ready(function() {
    $("#id_idRepuesto").attr("class","app-form-control");
    $("#id_nombreRepuesto").attr("class","app-form-control");
    $("#id_maquina").attr("class","form-control");
    $("#id_descripcionRepuesto").attr("class","app-form-control");
  
  });
  // funcion que se ejecuta cuando se presiona el boton enviar
  function mostrarAlerta(){
    //validacion de inputs vacios
    if(($("#id_idRepuesto").val()!="") && ($("#id_nombreRepuesto").val()!="") && ($("#id_descripcionRepuesto").val()!="") && ($("#id_maquina")!="")){
      $("#mensaje_alerta").show();
    }
    
  }

  function esconderAlerta(){    
    $("#mensaje_alerta").hide();    
  }

  $(function(){
    $('#form_agregar_repuestos').on('submit', function(event){
        event.preventDefault();
    });
});

