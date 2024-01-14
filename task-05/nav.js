class Header extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <nav>
        <h1>
          <a href="index.html">
            <img src="assets/navbar/logo.png" alt="Logo">
          </a>
        </h1>
        <ul>
          <li><a href="https://www.instagram.com/imaginedragons/">
            <img src="assets/navbar/instagram.svg" alt="Instagram">
          </a></li>
          <li><a href="https://twitter.com/Imaginedragons">
            <img src="assets/navbar/twitter.svg" alt="Twitter">
          </a></li>
          <li><a href="https://www.youtube.com/@ImagineDragons">
            <img src="assets/navbar/youtube.svg" alt="Youtube">
          </a></li>
          <li><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q">
            <img src="assets/navbar/spotify.png" alt="Spotify">
          </a></li>
        </ul>
      </nav>
    `;
  }
}

customElements.define('main-header', Header);
