export default {
  isLink(link) {
    return link.indexOf("http://") !== -1 || link.indexOf("https://") !== -1
  }
}
