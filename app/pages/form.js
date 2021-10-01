export default function Form(){
    return (
        <div>
            <span class="login100-form-title p-b-34 p-t-27">
                Confirme sua presença no culto
                {/* {#{ "{}/{}/{}".format(culto.dt_culto.day, culto.dt_culto.month, culto.dt_culto.year) }#} */}
            </span>
            {/* <!-- <p class="error">{{ form.errors }}</p> --> */}
            <div class="wrap-input100 validate-input" data-validate="Enter name">
                {/* <!-- <label for="nome">Inscrição individual</label> --> */}
                <input class="input100" type="text" name="nome" placeholder="seu nome" maxlength="20" />
                <span class="focus-input100" data-placeholder="&#xf207;"></span>
            </div>
            <div class="contact100-form">
                <select class="form-control" id="culto" name="culto">
                    {/* {% for c in form.culto %}
                        {{ c }}
                    {% endfor %} */}
                </select>
            </div>
            <br />
            <div class="container-login100-form-btn">
                <button name="action_save" class="login100-form-btn" type="submit">
                    Confirme
                </button>
            </div>
            {/* <span class="login100-form-title p-b-34 p-t-27">
                Nenhum culto disponível
            </span> */}
        </div>
    )
}