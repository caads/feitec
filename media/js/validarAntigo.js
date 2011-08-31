function validaArea()
	{
	if (document.form.area.value == "")
	{
  		alert('Digite a Área!');
  		document.form.area.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaNome()
	{
	if(document.form.nomeProj.value == "")
	{
  		alert('Digite o nome!');
  		document.form.nomeProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}


function validaResumo()
	{
	if (document.form.resumoProj.value == "")
	{
  		alert('Digite o Resumo!');
  		document.form.resumoProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaMaterialProj()
	{
	if (document.form.materialProj.value == "")
	{
  		alert('Digite o Material do Projeto!');
  		document.form.materialProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaCampus()
	{
	if (document.form.campusProj.value == "")
	{
  		alert('Digite o Campus!');
  		document.form.campusProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaSala()
	{
	if (document.form.salaProj.value == "")
	{
  		alert('Digite a Sala!');
  		document.form.salaProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaMaterialAV()
	{
	if (document.form.materialAVProj.value == "")
	{
  		alert('Digite o Material Áudio Visual!');
  		document.form.materialAVProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaCamposS()
	{
	if( (validaArea()) && (validaNome()) && (validaResumo()) && (validaMaterialProj()) && (validaCampus()) && (validaMaterialAV()))
	{
		document.form.situacaoProj.value = "Salvo";
		document.form.submit();
	}
	}

function validaCamposE()
	{
	if( (validaArea()) && (validaNome()) &&  (validaResumo()) && (validaMaterialProj()) && (validaCampus()) && (validaMaterialAV()))
	{
		document.form.situacaoProj.value = "Enviado";
		document.form.submit();
	}
	}
function validaCamposA()
	{
	if(validaSala())
	{
		document.form.situacaoProj.value = "Aprovado";
		document.form.submit();
	}
	}

function validaCamposN()
	{
	if(validaSala())
	{
		document.form.situacaoProj.value = "Não Aprovado";
		document.form.submit();
	}
	}

function imprimir(){

window.print()
}

function validarIntegrante()
	{
	if (document.formPrincipal.num.value == "")
	{
  		alert('Digite a quantidade de Integrantes!');
  		document.formPrincipal.num.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarProfessor()
	{
	if (document.formPrincipal.num2.value == "")
	{
  		alert('Digite a quantidade de Professores!');
  		document.formPrincipal.num2.focus();
     	return false;
	}
	else{
		return true;
		}
	}


function quantidadeIntegrante()
	{
	if (document.formPrincipal.num.value > 50)
	{
  		alert('Digite uma quantidade de Integrantes acessível!');
  		document.formPrincipal.num.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function quantidadeProfessor()
	{
	if (document.formPrincipal.num2.value > 50)
	{
  		alert('Digite uma quantidade de Professores acessívell!');
  		document.formPrincipal.num2.focus();
     	return false;
	}
	else{
		return true;
		}
	}


function Apenas_Numeros(caracter)
{
	var nTecla = 0;
	if (document.all) {
		nTecla = caracter.keyCode;
    }
	else
	{
     	nTecla = caracter.which;
    }
	if ((nTecla> 47 && nTecla <58)
    || nTecla == 8 || nTecla == 127
    || nTecla == 0 || nTecla == 9  // 0 == Tab
    || nTecla == 13) { // 13 == Enter
		return true;
    }
	else
	{
    	return false;
    }
}

function validaPrincipal()
	{
	if( (validarIntegrante()) && (validarProfessor()) && (quantidadeIntegrante()) && (quantidadeProfessor()))
	{
		document.formPrincipal.submit();
	}
	}

function  VerificaCPF(){
		if (vercpf(document.form.cpfInt.value)){
			return true;
		}
		else
			{
				alert('CPF INVALIDO');
				document.form.cpf.focus();	
				return false;			
			}
		}
	
	function vercpf (cpf) {
		if (cpf.length != 11 || cpf == "00000000000" || cpf == "11111111111" || cpf == "22222222222" || cpf == "33333333333" || cpf == "44444444444" || cpf == "55555555555" || cpf == "66666666666" || cpf == "77777777777" || cpf == "88888888888" || cpf == "99999999999")
		return false;		
		add = 0;
		for (i=0; i < 9; i ++)
			add += parseInt(cpf.charAt(i)) * (10 - i);
		rev = 11 - (add % 11);
		if (rev == 10 || rev == 11)
			rev = 0;
		if (rev != parseInt(cpf.charAt(9)))
		return false;
				
				
		add = 0;
		for (i = 0; i < 10; i ++)
			add += parseInt(cpf.charAt(i)) * (11 - i);
		rev = 11 - (add % 11);
		if (rev == 10 || rev == 11)
			rev = 0;
		if (rev != parseInt(cpf.charAt(10)))	
			return false;
		//alert('cpf valido.');
		return true;
}

function increment_form_ids(el, to, name) {
    var from = to-1
    $(':input', $(el)).each(function(i,e){
        var old_name = $(e).attr('name')
        var old_id = $(e).attr('id')
        $(e).attr('name', old_name.replace(from, to))
        $(e).attr('id', old_id.replace(from, to))
        $(e).val('')
    })
}

function add_inline_form(name) {
    var first = $('#id_'+name+'-0-id').parents('.inline-related')
    // check to see if this is a stacked or tabular inline
    if (first.hasClass("tabular")) {
        var field_table = first.parent().find('table > tbody')
        var count = field_table.children().length
        var copy = $('tr:last', field_table).clone(true)
        copy.removeClass("row1 row2")
        copy.addClass("row"+((count % 2) == 0 ? 1 : 2))
        field_table.append(copy)
        increment_form_ids($('tr:last', field_table), count, name)
    }
    else {
        var last = $(first).parent().children('.last-related')
        var copy = $(last).clone(true)
        var count = $(first).parent().children('.inline-related').length
        $(last).removeClass('last-related')
        var header = $('h3', copy)
        header.html(header.html().replace("#"+count, "#"+(count+1)))
        $(last).after(copy)
        increment_form_ids($(first).parents('.inline-group').children('.last-related'), count, name)
    }
    $('input#id_'+name+'-TOTAL_FORMS').val(count+1)
    return false;
}

// Add all the "Add Another" links to the bottom of each inline group
$(function() {
    var html_template = '<ul class="tools">'+
        '<li>'+
            '<a class="add" href="#" onclick="return add_inline_form(\'{{prefix}}\')">'+
            'Add another</a>'+
        '</li>'+
    '</ul>'
    $('.inline-group').each(function(i) {
        //prefix is in the name of the input fields before the "-"
        var prefix = $("input[type='hidden']", this).attr("name").split("-")[0]
        $(this).append(html_template.replace("{{prefix}}", prefix))
    })
})

