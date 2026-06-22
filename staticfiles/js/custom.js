document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 6 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            if (alert && alert.classList.contains('show')) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 6000);
    });

    // Form submission feedback
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Processing...';
            }
        });
    });

    // Animate stats counters on scroll
    const statValues = document.querySelectorAll('.dash-stat-value');
    if (statValues.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, { threshold: 0.5 });
        statValues.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(10px)';
            el.style.transition = 'all 0.6s ease';
            observer.observe(el);
        });
    }

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar-chesf');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 20) {
                navbar.style.boxShadow = '0 4px 20px rgba(15, 118, 110, 0.1)';
            } else {
                navbar.style.boxShadow = '0 1px 3px rgba(15, 118, 110, 0.08)';
            }
        });
    }
});
