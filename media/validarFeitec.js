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

function validarNomeEditar()
	{
	if (document.formAlterar.nomeProj.value == "")
	{
  		alert('Digite um nome ao projeto!');
  		document.formAlterar.nomeProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarCampusEditar()
	{
	if (document.formAlterar.campusProj.value == "")
	{
  		alert('Digite um campus ao Projeto!');
  		document.formAlterar.campusProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarAreaEditar()
	{
	if (document.formAlterar.area.value == "")
	{
  		alert('Digite uma área ao Projeto!');
  		document.formAlterar.area.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function EditarValidarCamposS()
	{
	if((validarNomeEditar()) && (validarCampusEditar()) && (validarAreaEditar()))
	{
		document.formAlterar.situacao.value = "Salvo";
		document.formAlterar.submit();
	}
	}


function validarCampus()
	{
	if (document.formProjeto.campusProj.value == "")
	{
  		alert('Digite um campus ao Projeto!');
  		document.formProjeto.campusProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarArea()
	{
	if (document.formProjeto.area.value == "")
	{
  		alert('Digite uma área ao Projeto!');
  		document.formProjeto.area.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarNome()
	{
	if (document.formProjeto.nomeProj.value == "")
	{
  		alert('Digite um nome ao projeto!');
  		document.formProjeto.nomeProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarCamposS()
	{
	if((validarNome()) && (validarCampus()) && (validarArea()))
	{
		document.formProjeto.situacao.value = "Salvo";
		document.formProjeto.submit();
	}
	}

function validarIntegrante()
    {
    if (document.formPrincipal.integrante.value == "")
    {
        alert('Digite um número para integrante');
        document.formPrincipal.integrante.focus();
        return false;
    }
    else{
        return true;
        }
    }

function validarProfessor()
    {
    if (document.formPrincipal.professor.value == "")
    {
        alert('Digite um número para integrante');
        document.formPrincipal.professor.focus();
        return false;
    }
    else{
        return true;
        }
    }

function quantidadeIntegrante()
    {
    if (document.formPrincipal.integrante.value > 50 || document.formPrincipal.integrante < 0)
    {
        alert('Digite um número para integrante');
        document.formPrincipal.integrante.focus();
        return false;
    }
    else{
        return true;
        }
    }

function quantidadeProfessor()
    {
    if (document.formPrincipal.professor.value > 50 || document.formPrincipal.professor < 0)
    {
        alert('Digite um número para integrante');
        document.formPrincipal.professor.focus();
        return false;
    }
    else{
        return true;
        }
    }

function validaPrincipal()
	{
	if( (validarIntegrante()) && (validarProfessor()) && (quantidadeIntegrante()) && (quantidadeProfessor()))
	{
		document.formPrincipal.submit();
	}
	}

function validarResumo()
    {
	if (document.formProjeto.resumoProj.value == "")
	{
  		alert('Digite um resumo ao projeto!');
  		document.formProjeto.resumoProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarMaterial()
    {
	if (document.formProjeto.materialProj.value == "")
	{
  		alert('Digite um material ao projeto!');
  		document.formProjeto.materialProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarEquipamento()
    {
	if (document.formProjeto.equipamentoProj.value == "")
	{
  		alert('Digite um equipamento ao projeto!');
  		document.formProjeto.equipamentoProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}


function validarCamposE()
	{
	if( (validarArea()) && (validarNome()) && (validarCampus()) && (validarResumo()) && (validarMaterial()) && (validarEquipamento()))
	{
		document.formProjeto.situacao.value = "Enviado";
		document.formProjeto.submit();
	}
	}


function validarResumoAlterar()
    {
	if (document.formAlterar.resumoProj.value == "")
	{
  		alert('Digite um resumo ao projeto!');
  		document.formAlterar.resumoProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarMaterialAlterar()
    {
	if (document.formAlterar.materialProj.value == "")
	{
  		alert('Digite um material ao projeto!');
  		document.formAlterar.materialProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validarEquipamentoAlterar()
    {
	if (document.formAlterar.equipamentoProj.value == "")
	{
  		alert('Digite um equipamento ao projeto!');
  		document.formAlterar.equipamentoProj.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function EditarValidarCamposE()
	{
	if( (validarAreaEditar()) && (validarNomeEditar()) && (validarCampusEditar()) && (validarResumoAlterar()) && (validarMaterialAlterar()) && (validarEquipamentoAlterar()))
	{
		document.formAlterar.situacao.value = "Enviado";
		document.formAlterar.submit();
	}
	}

function gerenciaAprovar()
    {
		document.formGerencia.situacao.value = "Aprovado";
		document.formGerencia.submit();
	}

function gerenciaReprovar()
    {
		document.formGerencia.situacao.value = "Reprovado";
		document.formGerencia.submit();
	}


function imprimir(){

window.print()
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

function Enviar()
    {
    document.formBloco.enviar.value = "Nao";
    document.formBloco.submit();
    }

function EnviarUsuario()
    {
    document.formBloco.enviar.value = "Enviar";
    document.formBloco.submit();
    }

function formata_data(caracter) {
    var nTecla = 0;
	if (document.all) {
		nTecla = caracter.keyCode;
    }
	else
	{
     	nTecla = caracter.which;
    }
    if( nTecla == 8 ){
        return true;
    }
    else{
    switch (document.form.dataCert.value.length) {
        case 2:
                document.form.dataCert.value = document.form.dataCert.value + "/";
                break;
        case 5:
                document.form.dataCert.value = document.form.dataCert.value + "/";
                break;
}
}
}
