export default function Form(){
    return (
        <div>
            <span className="login100-form-title p-b-34 p-t-27">
                Confirme sua presença no culto
                {/* {#{ "{}/{}/{}".format(culto.dt_culto.day, culto.dt_culto.month, culto.dt_culto.year) }#} */}
            </span>
            {/* <!-- <p className="error">{{ form.errors }}</p> --> */}
            <div className="wrap-input100 validate-input" data-validate="Enter name">
                {/* <!-- <label for="nome">Inscrição individual</label> --> */}
                <input className="input100" type="text" name="nome" placeholder="seu nome" />
                <span className="focus-input100" data-placeholder="&#xf207;"></span>
            </div>
            <div className="contact100-form">
                <select className="form-control" id="culto" name="culto">
                    {/* {% for c in form.culto %}
                        {{ c }}
                    {% endfor %} */}
                </select>
            </div>
            <br />
            <div className="container-login100-form-btn">
                <button name="action_save" className="login100-form-btn" type="submit">
                    Confirme
                </button>
            </div>
            {/* <span className="login100-form-title p-b-34 p-t-27">
                Nenhum culto disponível
            </span> */}
        </div>
    )
}