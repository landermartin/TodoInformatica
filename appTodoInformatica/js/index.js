function generarCodigo(max) {
    let r='';
    for (let i=0;i<max/13;i++)
      r+=(Math.random()+1).toString(16).substring(2);
    return r.substring(0,max).toUpperCase();
  }