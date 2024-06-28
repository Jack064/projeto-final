function somente_numero(e){
    tecla = (window.Event) ? e.which : e.keyCode;
    if (tecla > 47 && tecla < 58){
        return true;
    }
    else{
        if (tecla > 95 && tecla < 106){
            return true;
        }
        else{
            if (tecla == 8 || tecla == 46 || tecla == 37 || tecla == 39){
                return true;
            }
            else{
                return false
            }
        }
    }
}

function mascara_tel(objeto){
    if(objeto.value.length == 0){
        objeto.value = objeto.value + '('
    }
    if(objeto.value.length == 3){
        objeto.value = objeto.value + ')'
    }
}