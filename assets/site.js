(function () {
  "use strict";

  var EVENT_NAME = "codex-lp-analytics";

  function emit(name, properties) {
    var detail = {
      event: name,
      properties: properties || {},
      timestamp: new Date().toISOString()
    };

    window.codexLpEventQueue = window.codexLpEventQueue || [];
    window.codexLpEventQueue.push(detail);
    window.dispatchEvent(new CustomEvent(EVENT_NAME, { detail: detail }));
  }

  function setStatus(element, message, state) {
    if (!element) return;
    element.textContent = message;
    element.dataset.state = state || "idle";
  }

  function fallbackCopy(text) {
    var textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.appendChild(textarea);
    textarea.select();

    try {
      if (!document.execCommand("copy")) throw new Error("copy-not-supported");
    } finally {
      textarea.remove();
    }
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    return Promise.resolve().then(function () {
      fallbackCopy(text);
    });
  }

  function setupCopyButton(button) {
    var status = document.getElementById(button.dataset.statusTarget);
    var defaultLabel = button.textContent;
    var timer;
    var busy = false;

    if (!status || !button.dataset.copyUrl) return;

    button.addEventListener("click", function () {
      if (busy) return;

      window.clearTimeout(timer);
      busy = true;
      button.setAttribute("aria-busy", "true");
      setStatus(status, "ファイルを読み込んでいます…", "progress");

      fetch(button.dataset.copyUrl, {
        credentials: "same-origin",
        cache: "no-store"
      })
        .then(function (response) {
          if (!response.ok) throw new Error("http_" + response.status);
          return response.text();
        })
        .then(copyText)
        .then(function () {
          button.textContent = "コピーしました";
          setStatus(
            status,
            button.dataset.fileName + "の全文をコピーしました。Codexへ貼り付けてください。",
            "success"
          );
          emit("codex_lp_file_copy", {
            file_name: button.dataset.fileName,
            version: "2.0.1"
          });
        })
        .catch(function () {
          button.textContent = "コピーできませんでした";
          setStatus(
            status,
            "自動コピーに失敗しました。ダウンロードしたファイルを開き、全文を手動でコピーしてください。",
            "error"
          );
          emit("codex_lp_copy_failure", {
            file_name: button.dataset.fileName,
            error_code: "clipboard_or_fetch_unavailable"
          });
        })
        .finally(function () {
          busy = false;
          button.removeAttribute("aria-busy");
          button.focus({ preventScroll: true });
          timer = window.setTimeout(function () {
            button.textContent = defaultLabel;
          }, 2200);
        });
    });
  }

  function setupDownload(link) {
    var status = document.getElementById(link.dataset.statusTarget);
    var expectedSize = Number(link.dataset.expectedSize);
    var busy = false;

    link.addEventListener("click", function (event) {
      if (busy || !window.fetch || !window.URL || !window.Blob) return;

      event.preventDefault();
      busy = true;
      link.setAttribute("aria-disabled", "true");
      setStatus(status, "ZIPを確認しています…", "progress");

      fetch(link.href, { credentials: "same-origin", cache: "no-store" })
        .then(function (response) {
          if (!response.ok) throw new Error("http_" + response.status);
          return response.blob();
        })
        .then(function (blob) {
          if (expectedSize && blob.size !== expectedSize) {
            throw new Error("size_mismatch");
          }

          var objectUrl = URL.createObjectURL(blob);
          var temporaryLink = document.createElement("a");
          temporaryLink.href = objectUrl;
          temporaryLink.download = link.getAttribute("download");
          document.body.appendChild(temporaryLink);
          temporaryLink.click();
          temporaryLink.remove();
          window.setTimeout(function () { URL.revokeObjectURL(objectUrl); }, 1000);
          setStatus(
            status,
            "ダウンロードを開始しました。完了はブラウザのダウンロード一覧で確認してください。",
            "success"
          );
          emit("codex_lp_package_download", { version: link.dataset.version });
        })
        .catch(function (error) {
          setStatus(
            status,
            "取得できませんでした。個別のMarkdownをダウンロードするか、受取ヘルプをご覧ください。",
            "error"
          );
          emit("codex_lp_download_error", {
            version: link.dataset.version,
            error_code: error.message === "size_mismatch" ? "size_mismatch" : "fetch_failed"
          });
        })
        .finally(function () {
          busy = false;
          link.removeAttribute("aria-disabled");
        });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-copy-url]").forEach(setupCopyButton);
    document.querySelectorAll("[data-download]").forEach(setupDownload);

    emit("codex_lp_view", { path: window.location.pathname, version: "2.0.1" });

    document.querySelectorAll("[data-file-download]").forEach(function (link) {
      link.addEventListener("click", function () {
        emit("codex_lp_file_download", {
          file_name: link.dataset.fileName,
          version: "2.0.1"
        });
      });
    });

    document.querySelectorAll("[data-help-link]").forEach(function (link) {
      link.addEventListener("click", function () {
        emit("codex_lp_help_open", { placement: link.dataset.placement });
      });
    });

    document.querySelectorAll("[data-changelog-link]").forEach(function (link) {
      link.addEventListener("click", function () {
        emit("codex_lp_changelog_open", { version: "2.0.1" });
      });
    });
  });
})();
