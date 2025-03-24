// Alpine.js data and functions
document.addEventListener('alpine:init', () => {
    Alpine.data('sidebarState', () => ({
        sidebarOpen: true,
        toggleSidebar() {
            this.sidebarOpen = !this.sidebarOpen;
        }
    }));

    Alpine.data('dropdownState', () => ({
        open: false,
        toggle() {
            this.open = !this.open;
        },
        close() {
            this.open = false;
        }
    }));
});

// Custom utility functions
function initializeApp() {
    // Add any initialization logic here
    console.log('Application initialized');
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', initializeApp);