function generarCodigo(max) {
    let r='';
    for (let i=0;i<max/13;i++)
      r+=(Math.random()+1).toString(16).substring(2);
    return r.substring(0,max).toUpperCase();
  }

  $(document).ready(function(){
      $("#imagenDados").click(function(){
        if (Math.floor(Math.random() * 100) <= 20) {
          const cod = generarCodigo(6);
          $("#codigoPromocion").text("Enhorabuena! Tu código es #" + cod); // establecer mensaje
          $("#codigoPromocion").show(); // mostrar mensaje
          $("#imagenDados").hide(); // quitar los dados
        } else {
          $("#codigoPromocion").text("Vaya! No ha habido suerte :("); // establecer mensaje
          $("#codigoPromocion").show(); // mostrar mensaje
          $("#imagenDados").hide(); // quitar los dados
        }
      });
  });