import React from 'react'
import "./styles/footer.css"
import { NavLink } from 'react-router-dom'

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-main-container">
                <div id="footer-dev-title">Developers</div>
                <NavLink className="footer-dev-name-link" to="/about">Click here for more About the Developers</NavLink>
                <div className="footer-devs-container">
                    <div className="footer-dev">
                        <NavLink className="footer-dev-name-link" to="/about">
                            <div className="footer-dev-name" >jane Martin</div>
                        </NavLink>
                        <a className="footer-dev-link" href="https://github.com/jemcodes">github</a>
                        <a className="footer-dev-link" href="https://www.linkedin.com/in/jemcodes/">linkedin</a>
                    </div>
                    <div className="footer-dev">
                        <NavLink className="footer-dev-name-link" to="/about">
                            <div className="footer-dev-name" >Lisa Noor</div>
                        </NavLink>
                        <a className="footer-dev-link" href="https://github.com/Skulllady">github</a>
                        <a className="footer-dev-link" href="https://www.linkedin.com/in/lisa-noor-hoque-976120208/">linkedin</a>
                    </div>
                    <div className="footer-dev">
                        <NavLink className="footer-dev-name-link" to="/about">
                            <div className="footer-dev-name" >Patrick Nusbaum</div>
                        </NavLink>
                        <a className="footer-dev-link" href="https://github.com/patricknuttree">github</a>
                        <a className="footer-dev-link" href="www.linkedin.com/in/patrick-nusbaum-mpa">linkedin</a>
                    </div>
                    <div className="footer-dev">
                        <NavLink className="footer-dev-name-link" to="/about">
                            <div className="footer-dev-name" >Jamie Sullivan</div>
                        </NavLink>
                        <a className="footer-dev-link" href="https://github.com/bilbopicard">github</a>
                        <a className="footer-dev-link" href="https://www.linkedin.com/in/sullivan-jamie/">linkedin</a>
                    </div>
                </div>
            </div>
        </footer>

    )
}

export default Footer;