"""
Main Window V2 - Sidebar Navigation with Dashboard
Theophysics Research Manager - Enhanced Edition
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Optional

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QStatusBar, QFileDialog, QMessageBox, QListWidget, QListWidgetItem,
    QStackedWidget, QSplitter, QGroupBox, QLineEdit, QPushButton,
    QProgressBar, QScrollArea, QFrame, QCheckBox, QComboBox,
    QTableWidget, QTableWidgetItem, QHeaderView, QTextEdit,
    QGridLayout, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon

from .styles_v2 import DARK_THEME_V2, COLORS

if TYPE_CHECKING:
    from core_v2.settings_manager import SettingsManager
    from core_v2.obsidian_definitions_manager import ObsidianDefinitionsManager
    from core_v2.vault_system_installer import VaultSystemInstaller
    from core_v2.global_analytics_aggregator import GlobalAnalyticsAggregator
    from core_v2.research_linker import ResearchLinker
    from core_v2.footnote_system import FootnoteSystem
    from core_v2.postgres_manager import PostgresManager


class MainWindowV2(QMainWindow):
    """
    Enhanced main window with sidebar navigation.
    """
    
    NAV_ITEMS = [
        ("🏠", "Dashboard"),
        ("📄", "Paper Scanner"),
        ("📖", "Definition Scanner"),
        ("🔗", "Auto-Linker"),
        ("📚", "Definitions"),
        ("🏗️", "Vault System"),
        ("📊", "Data Aggregation"),
        ("🔗", "Research Links"),
        ("📝", "Footnotes"),
        ("🗄️", "Database"),
        ("⚙️", "Settings"),
    ]
    
    def __init__(
        self,
        settings: SettingsManager,
        definitions_manager: ObsidianDefinitionsManager,
        vault_installer: VaultSystemInstaller,
        global_aggregator: GlobalAnalyticsAggregator,
        research_linker: ResearchLinker,
        footnote_system: FootnoteSystem,
        postgres_manager: PostgresManager
    ):
        super().__init__()
        self.settings = settings
        self.definitions_manager = definitions_manager
        self.vault_installer = vault_installer
        self.global_aggregator = global_aggregator
        self.research_linker = research_linker
        self.footnote_system = footnote_system
        self.postgres_manager = postgres_manager
        
        # Scan worker reference
        self._scan_worker = None
        
        # Folder configuration
        self._folder_config: Dict[str, str] = {}
        self._load_folder_config()
        
        self.setWindowTitle("🔬 Theophysics Research Manager v2")
        self.setGeometry(100, 100, 1500, 950)
        self.setMinimumSize(1200, 800)
        
        self._setup_ui()
        self._setup_status_bar()
    
    def _load_folder_config(self):
        """Load configured folders from settings."""
        config_path = Path(__file__).parent.parent / "config" / "folders.json"
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    self._folder_config = json.load(f)
            except:
                pass
        
        # Defaults
        defaults = {
            'vault_root': self.settings.get('obsidian', 'vault_path', ''),
            'glossary': self.settings.get('obsidian', 'definitions_folder', ''),
            'logos_papers': '',
            'evidence_bundles': '',
            'analytics': '',
            'notes': '',
        }
        for key, val in defaults.items():
            if key not in self._folder_config:
                self._folder_config[key] = val
    
    def _save_folder_config(self):
        """Save folder configuration."""
        config_path = Path(__file__).parent.parent / "config" / "folders.json"
        config_path.parent.mkdir(exist_ok=True)
        with open(config_path, 'w') as f:
            json.dump(self._folder_config, f, indent=2)
    
    def _setup_ui(self):
        """Setup the main UI with sidebar."""
        self.setStyleSheet(DARK_THEME_V2)
        
        central = QWidget()
        self.setCentralWidget(central)
        
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # === SIDEBAR ===
        sidebar = QWidget()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet(f"background-color: {COLORS['bg_dark']};")
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)
        
        # Logo/Title
        title_container = QWidget()
        title_container.setStyleSheet(f"""
            background-color: {COLORS['bg_dark']};
            border-bottom: 1px solid {COLORS['border_dark']};
        """)
        title_layout = QVBoxLayout(title_container)
        title_layout.setContentsMargins(16, 20, 16, 20)
        
        title_label = QLabel("🔬 Theophysics")
        title_label.setStyleSheet(f"""
            font-size: 16pt;
            font-weight: bold;
            color: {COLORS['accent_cyan']};
            background: transparent;
        """)
        title_layout.addWidget(title_label)
        
        subtitle = QLabel("Research Manager")
        subtitle.setStyleSheet(f"""
            font-size: 10pt;
            color: {COLORS['text_muted']};
            background: transparent;
        """)
        title_layout.addWidget(subtitle)
        
        sidebar_layout.addWidget(title_container)
        
        # Navigation list
        self.nav_list = QListWidget()
        self.nav_list.setObjectName("sidebar")
        self.nav_list.setIconSize(QSize(20, 20))
        
        for icon, name in self.NAV_ITEMS:
            item = QListWidgetItem(f"{icon}  {name}")
            item.setSizeHint(QSize(200, 44))
            self.nav_list.addItem(item)
        
        self.nav_list.setCurrentRow(0)
        self.nav_list.currentRowChanged.connect(self._on_nav_changed)
        
        sidebar_layout.addWidget(self.nav_list)
        sidebar_layout.addStretch()
        
        # Version info at bottom
        version_label = QLabel("v2.1.0")
        version_label.setStyleSheet(f"""
            color: {COLORS['text_muted']};
            padding: 12px;
            font-size: 9pt;
            background: transparent;
        """)
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(version_label)
        
        main_layout.addWidget(sidebar)
        
        # === SEPARATOR LINE ===
        separator = QFrame()
        separator.setFixedWidth(1)
        separator.setStyleSheet(f"background-color: {COLORS['border_dark']};")
        main_layout.addWidget(separator)
        
        # === CONTENT AREA ===
        self.page_stack = QStackedWidget()
        main_layout.addWidget(self.page_stack)
        
        # Build pages
        self._build_dashboard_page()      # 0
        self._build_paper_scanner_page()  # 1
        self._build_definition_scanner_page()    # 2
        self._build_linker_page()         # 3 - New Linker
        self._build_definitions_page()    # 4
        self._build_vault_system_page()   # 4
        self._build_aggregation_page()    # 5
        self._build_research_links_page() # 6
        self._build_footnotes_page()      # 7
        self._build_database_page()       # 8
        self._build_settings_page()       # 9
    
    def _on_nav_changed(self, index: int):
        """Handle navigation selection."""
        self.page_stack.setCurrentIndex(index)
    
    def _create_page_container(self, title: str) -> tuple[QWidget, QVBoxLayout]:
        """Create a standard page container with scroll area."""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Page header
        header = QLabel(title)
        header.setStyleSheet(f"""
            font-size: 24pt;
            font-weight: bold;
            color: {COLORS['text_primary']};
            padding-bottom: 10px;
        """)
        layout.addWidget(header)
        
        scroll.setWidget(page)
        self.page_stack.addWidget(scroll)
        
        return page, layout
    
    # ==========================================
    # PAGE 0: DASHBOARD
    # ==========================================
    def _build_dashboard_page(self):
        """Build the dashboard/home page with folder configuration."""
        page, layout = self._create_page_container("🏠 Dashboard")
        
        # Two-column layout
        columns = QHBoxLayout()
        columns.setSpacing(20)
        
        # === LEFT COLUMN: Folder Configuration ===
        left_col = QVBoxLayout()
        left_col.setSpacing(15)
        
        folders_group = QGroupBox("📁 Configured Folders")
        folders_layout = QVBoxLayout(folders_group)
        folders_layout.setSpacing(12)
        
        # Folder entries
        self._folder_inputs = {}
        
        folder_definitions = [
            ('vault_root', 'Vault Root', 'Main Obsidian vault path'),
            ('glossary', 'Glossary', 'Definitions folder'),
            ('logos_papers', 'Logos Papers', '12 main research papers'),
            ('evidence_bundles', 'Evidence Bundles', 'Supporting evidence'),
            ('analytics', 'Analytics Output', 'Generated analytics'),
            ('notes', 'Working Notes', 'Daily notes / scratch'),
        ]
        
        for key, label, hint in folder_definitions:
            row = QHBoxLayout()
            
            lbl = QLabel(f"{label}:")
            lbl.setFixedWidth(120)
            lbl.setStyleSheet(f"color: {COLORS['text_secondary']};")
            row.addWidget(lbl)
            
            edit = QLineEdit()
            edit.setPlaceholderText(hint)
            edit.setText(self._folder_config.get(key, ''))
            self._folder_inputs[key] = edit
            row.addWidget(edit)
            
            browse_btn = QPushButton("...")
            browse_btn.setFixedWidth(40)
            browse_btn.clicked.connect(lambda checked, k=key: self._browse_folder(k))
            row.addWidget(browse_btn)
            
            folders_layout.addLayout(row)
        
        # Save button
        save_folders_btn = QPushButton("💾 Save Configuration")
        save_folders_btn.setProperty("class", "primary")
        save_folders_btn.clicked.connect(self._save_folders_clicked)
        folders_layout.addWidget(save_folders_btn)
        
        left_col.addWidget(folders_group)
        
        # === Scan Controls ===
        scan_group = QGroupBox("🔍 Scan Controls")
        scan_layout = QVBoxLayout(scan_group)
        
        # Scope selector
        scope_row = QHBoxLayout()
        scope_row.addWidget(QLabel("Scan Scope:"))
        
        self.scan_scope_combo = QComboBox()
        self.scan_scope_combo.addItems([
            "Entire Vault",
            "Glossary Only",
            "Logos Papers Only",
            "Evidence Bundles Only",
            "Custom Folder..."
        ])
        scope_row.addWidget(self.scan_scope_combo)
        scan_layout.addLayout(scope_row)
        
        # Recursive checkbox
        self.recursive_check = QCheckBox("Scan recursively (all subfolders)")
        self.recursive_check.setChecked(True)
        scan_layout.addWidget(self.recursive_check)
        
        # Thread count
        thread_row = QHBoxLayout()
        thread_row.addWidget(QLabel("Parallel threads:"))
        self.thread_combo = QComboBox()
        self.thread_combo.addItems(["4", "8", "12", "16"])
        self.thread_combo.setCurrentText("8")
        thread_row.addWidget(self.thread_combo)
        thread_row.addStretch()
        scan_layout.addLayout(thread_row)
        
        # Scan buttons
        btn_row = QHBoxLayout()
        
        self.full_scan_btn = QPushButton("🚀 Full Scan")
        self.full_scan_btn.setProperty("class", "success")
        self.full_scan_btn.clicked.connect(self._start_full_scan)
        btn_row.addWidget(self.full_scan_btn)
        
        self.quick_scan_btn = QPushButton("⚡ Quick Stats")
        self.quick_scan_btn.clicked.connect(self._start_quick_scan)
        btn_row.addWidget(self.quick_scan_btn)
        
        self.cancel_scan_btn = QPushButton("✖ Cancel")
        self.cancel_scan_btn.setProperty("class", "danger")
        self.cancel_scan_btn.setEnabled(False)
        self.cancel_scan_btn.clicked.connect(self._cancel_scan)
        btn_row.addWidget(self.cancel_scan_btn)
        
        scan_layout.addLayout(btn_row)
        
        # Progress
        self.scan_progress = QProgressBar()
        self.scan_progress.setVisible(False)
        scan_layout.addWidget(self.scan_progress)
        
        self.scan_status_label = QLabel("Ready")
        self.scan_status_label.setStyleSheet(f"color: {COLORS['text_muted']};")
        scan_layout.addWidget(self.scan_status_label)
        
        left_col.addWidget(scan_group)
        left_col.addStretch()
        
        columns.addLayout(left_col, 1)
        
        # === RIGHT COLUMN: Statistics ===
        right_col = QVBoxLayout()
        right_col.setSpacing(15)
        
        stats_group = QGroupBox("📊 Vault Statistics")
        stats_layout = QGridLayout(stats_group)
        stats_layout.setSpacing(15)
        
        # Stats cards
        self._stat_labels = {}
        stat_items = [
            ('total_files', '📄 Total Notes', '0'),
            ('total_words', '📝 Total Words', '0'),
            ('unique_tags', '🏷️ Unique Tags', '0'),
            ('unique_links', '🔗 Unique Links', '0'),
            ('glossary_count', '📖 Definitions', '0'),
            ('logos_count', '📑 Logos Papers', '0'),
        ]
        
        for i, (key, label, default) in enumerate(stat_items):
            row, col = divmod(i, 2)
            
            card = QFrame()
            card.setStyleSheet(f"""
                background-color: {COLORS['bg_medium']};
                border-radius: 8px;
                padding: 15px;
            """)
            card_layout = QVBoxLayout(card)
            
            value_label = QLabel(default)
            value_label.setStyleSheet(f"""
                font-size: 28pt;
                font-weight: bold;
                color: {COLORS['accent_cyan']};
            """)
            value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            card_layout.addWidget(value_label)
            self._stat_labels[key] = value_label
            
            name_label = QLabel(label)
            name_label.setStyleSheet(f"color: {COLORS['text_secondary']}; font-size: 10pt;")
            name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            card_layout.addWidget(name_label)
            
            stats_layout.addWidget(card, row, col)
        
        right_col.addWidget(stats_group)
        
        # Folder breakdown
        breakdown_group = QGroupBox("📁 Folder Breakdown")
        breakdown_layout = QVBoxLayout(breakdown_group)
        
        self.folder_table = QTableWidget()
        self.folder_table.setColumnCount(3)
        self.folder_table.setHorizontalHeaderLabels(["Folder", "Files", "% of Total"])
        self.folder_table.horizontalHeader().setStretchLastSection(True)
        self.folder_table.setMaximumHeight(200)
        breakdown_layout.addWidget(self.folder_table)
        
        right_col.addWidget(breakdown_group)
        
        # Recent activity
        activity_group = QGroupBox("🕐 Recent Activity")
        activity_layout = QVBoxLayout(activity_group)
        
        self.activity_list = QListWidget()
        self.activity_list.setMaximumHeight(150)
        activity_layout.addWidget(self.activity_list)
        
        right_col.addWidget(activity_group)
        right_col.addStretch()
        
        columns.addLayout(right_col, 1)
        layout.addLayout(columns)
    
    def _browse_folder(self, key: str):
        """Browse for a folder."""
        current = self._folder_inputs[key].text()
        folder = QFileDialog.getExistingDirectory(self, f"Select {key} folder", current)
        if folder:
            self._folder_inputs[key].setText(folder)
    
    def _save_folders_clicked(self):
        """Save folder configuration."""
        for key, edit in self._folder_inputs.items():
            self._folder_config[key] = edit.text()
        
        self._save_folder_config()
        
        # Update settings manager too
        if self._folder_config.get('vault_root'):
            self.settings.set('obsidian', 'vault_path', self._folder_config['vault_root'])
        if self._folder_config.get('glossary'):
            self.settings.set('obsidian', 'definitions_folder', self._folder_config['glossary'])
        
        QMessageBox.information(self, "Saved", "Folder configuration saved!")
    
    def _get_scan_path(self) -> Optional[Path]:
        """Get the path to scan based on scope selection."""
        scope = self.scan_scope_combo.currentText()
        
        if scope == "Entire Vault":
            path = self._folder_config.get('vault_root')
        elif scope == "Glossary Only":
            path = self._folder_config.get('glossary')
        elif scope == "Logos Papers Only":
            path = self._folder_config.get('logos_papers')
        elif scope == "Evidence Bundles Only":
            path = self._folder_config.get('evidence_bundles')
        else:
            # Custom folder
            path = QFileDialog.getExistingDirectory(self, "Select folder to scan")
        
        if path and Path(path).exists():
            return Path(path)
        return None
    
    def _start_full_scan(self):
        """Start a full vault scan."""
        scan_path = self._get_scan_path()
        if not scan_path:
            QMessageBox.warning(self, "No Path", "Please configure the folder path first.")
            return
        
        # Import here to avoid circular imports
        from core.threaded_scanner import ScanWorker
        
        # Disable buttons, show progress
        self.full_scan_btn.setEnabled(False)
        self.quick_scan_btn.setEnabled(False)
        self.cancel_scan_btn.setEnabled(True)
        self.scan_progress.setVisible(True)
        self.scan_progress.setValue(0)
        self.scan_status_label.setText(f"Starting scan of {scan_path.name}...")
        self.scan_status_label.setStyleSheet(f"color: {COLORS['accent_cyan']};")
        
        # Create worker
        max_workers = int(self.thread_combo.currentText())
        recursive = self.recursive_check.isChecked()
        
        self._scan_worker = ScanWorker(
            scan_path=scan_path,
            recursive=recursive,
            max_workers=max_workers
        )
        
        # Connect signals
        self._scan_worker.progress.connect(self._on_scan_progress)
        self._scan_worker.finished.connect(self._on_scan_finished)
        self._scan_worker.error.connect(self._on_scan_error)
        
        # Start
        self._scan_worker.start()
    
    def _start_quick_scan(self):
        """Start a quick metadata-only scan."""
        scan_path = self._get_scan_path()
        if not scan_path:
            QMessageBox.warning(self, "No Path", "Please configure the folder path first.")
            return
        
        from core.threaded_scanner import QuickScanWorker
        
        self.full_scan_btn.setEnabled(False)
        self.quick_scan_btn.setEnabled(False)
        self.cancel_scan_btn.setEnabled(True)
        self.scan_progress.setVisible(True)
        self.scan_progress.setMaximum(0)  # Indeterminate
        self.scan_status_label.setText("Quick scan...")
        
        self._scan_worker = QuickScanWorker(
            scan_path=scan_path,
            recursive=self.recursive_check.isChecked()
        )
        self._scan_worker.progress.connect(lambda p, f: self.scan_status_label.setText(f"Scanning {f}..."))
        self._scan_worker.finished.connect(self._on_quick_scan_finished)
        self._scan_worker.error.connect(self._on_scan_error)
        self._scan_worker.start()
    
    def _cancel_scan(self):
        """Cancel the running scan."""
        if self._scan_worker:
            self._scan_worker.cancel()
            self._scan_worker = None
        
        self._reset_scan_ui()
        self.scan_status_label.setText("Scan cancelled")
        self.scan_status_label.setStyleSheet(f"color: {COLORS['accent_orange']};")
    
    def _reset_scan_ui(self):
        """Reset scan UI to ready state."""
        self.full_scan_btn.setEnabled(True)
        self.quick_scan_btn.setEnabled(True)
        self.cancel_scan_btn.setEnabled(False)
        self.scan_progress.setVisible(False)
        self.scan_progress.setMaximum(100)
    
    def _on_scan_progress(self, percent: int, current_file: str):
        """Handle scan progress update."""
        self.scan_progress.setValue(percent)
        self.scan_status_label.setText(f"{percent}% - {current_file}")
    
    def _on_scan_finished(self, result):
        """Handle scan completion."""
        self._reset_scan_ui()
        
        # Update stats
        self._stat_labels['total_files'].setText(f"{result.total_files:,}")
        self._stat_labels['total_words'].setText(f"{result.total_words:,}")
        self._stat_labels['unique_tags'].setText(f"{len(result.unique_tags):,}")
        self._stat_labels['unique_links'].setText(f"{len(result.unique_links):,}")
        
        # Update folder breakdown table
        self.folder_table.setRowCount(len(result.folder_stats))
        for i, (folder, count) in enumerate(sorted(result.folder_stats.items(), key=lambda x: -x[1])):
            self.folder_table.setItem(i, 0, QTableWidgetItem(folder))
            self.folder_table.setItem(i, 1, QTableWidgetItem(str(count)))
            pct = (count / result.total_files * 100) if result.total_files else 0
            self.folder_table.setItem(i, 2, QTableWidgetItem(f"{pct:.1f}%"))
        
        # Status
        duration = result.duration_seconds
        self.scan_status_label.setText(
            f"✓ Scan complete: {result.total_files:,} files in {duration:.1f}s "
            f"({len(result.errors)} errors)"
        )
        self.scan_status_label.setStyleSheet(f"color: {COLORS['accent_green']};")
        
        # Add to activity
        from datetime import datetime
        self.activity_list.insertItem(0, f"{datetime.now().strftime('%H:%M:%S')} - Scanned {result.total_files} files")
        
        self._scan_worker = None
    
    def _on_quick_scan_finished(self, result: dict):
        """Handle quick scan completion."""
        self._reset_scan_ui()
        
        self._stat_labels['total_files'].setText(f"{result['total_files']:,}")
        
        size_mb = result['total_size_bytes'] / (1024 * 1024)
        self.scan_status_label.setText(
            f"✓ Quick scan: {result['total_files']:,} files, {size_mb:.1f} MB total"
        )
        self.scan_status_label.setStyleSheet(f"color: {COLORS['accent_green']};")
        
        self._scan_worker = None
    
    def _on_scan_error(self, error_msg: str):
        """Handle scan error."""
        self._reset_scan_ui()
        self.scan_status_label.setText(f"✖ Error: {error_msg}")
        self.scan_status_label.setStyleSheet(f"color: {COLORS['accent_red']};")
        QMessageBox.critical(self, "Scan Error", error_msg)
        self._scan_worker = None
    
    # ==========================================
    # PAGE 1: PAPER SCANNER
    # ==========================================
    def _build_paper_scanner_page(self):
        """Build the paper scanner page."""
        page, layout = self._create_page_container("📄 Paper Scanner")
        
        info = QLabel("Scan papers to find terms needing definitions.")
        info.setStyleSheet(f"color: {COLORS['text_secondary']};")
        layout.addWidget(info)
        
        # Folder selection
        folder_group = QGroupBox("Select Folder to Scan")
        folder_layout = QHBoxLayout(folder_group)
        
        self.paper_scan_path = QLineEdit()
        self.paper_scan_path.setPlaceholderText("Select folder containing papers...")
        folder_layout.addWidget(self.paper_scan_path)
        
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(self._browse_paper_folder)
        folder_layout.addWidget(browse_btn)
        
        use_logos_btn = QPushButton("Use Logos Papers")
        use_logos_btn.setProperty("class", "primary")
        use_logos_btn.clicked.connect(lambda: self.paper_scan_path.setText(
            self._folder_config.get('logos_papers', '')
        ))
        folder_layout.addWidget(use_logos_btn)
        
        layout.addWidget(folder_group)
        
        # Options
        options_group = QGroupBox("Scan Options")
        options_layout = QVBoxLayout(options_group)
        
        self.paper_recursive = QCheckBox("Scan recursively (all subfolders)")
        self.paper_recursive.setChecked(True)
        options_layout.addWidget(self.paper_recursive)
        
        self.paper_nlp = QCheckBox("Enable NLP (extract complex terms)")
        options_layout.addWidget(self.paper_nlp)
        
        layout.addWidget(options_group)
        
        # Scan button
        scan_btn = QPushButton("🚀 SCAN SELECTED PAPERS")
        scan_btn.setProperty("class", "success")
        scan_btn.setMinimumHeight(50)
        scan_btn.clicked.connect(self._scan_papers)
        layout.addWidget(scan_btn)
        
        # Results area
        results_group = QGroupBox("📋 Found Terms")
        results_layout = QVBoxLayout(results_group)
        
        self.paper_results_table = QTableWidget()
        self.paper_results_table.setColumnCount(5)
        self.paper_results_table.setHorizontalHeaderLabels([
            "Term", "Type", "Count", "Status", "Action"
        ])
        self.paper_results_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        results_layout.addWidget(self.paper_results_table)
        
        layout.addWidget(results_group)
        layout.addStretch()
    
    def _browse_paper_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Papers Folder")
        if folder:
            self.paper_scan_path.setText(folder)
    
    def _scan_papers(self):
        """Scan papers for undefined terms."""
        path = self.paper_scan_path.text()
        if not path or not Path(path).exists():
            QMessageBox.warning(self, "No Folder", "Please select a valid folder.")
        QMessageBox.information(self, "Scanning", f"Would scan: {path}\n(Implementation pending)")
    
    # ==========================================
    # PAGE 2: DEFINITION SCANNER
    # ==========================================
    def _build_definition_scanner_page(self):
        """Build the definition scanner page."""
        page, layout = self._create_page_container("📖 Definition Scanner")
        
        info = QLabel("Scan vault for terms that look like definitions but aren't indexed.")
        info.setStyleSheet(f"color: {COLORS['text_secondary']};")
        layout.addWidget(info)
        
        # Placeholder
        btn = QPushButton("Scan for Definitions")
        btn.setEnabled(False)
        layout.addWidget(btn)
        
        layout.addStretch()

    # ==========================================
    # PAGE 3: AUTO-LINKER (ENHANCED & THREADED)
    # ==========================================
    def _build_linker_page(self):
        """Build the Auto-Linker and Entity Extraction page."""
        page, layout = self._create_page_container("🔗 Auto-Linker & Entity Extraction")
        
        # Description
        desc = QLabel(
            "Scan your files for key terms (Biblical references, theological concepts, people) found in your vault or footnotes.yaml. "
            "The process happens in two steps: 1. Scan to find candidates. 2. Review and Apply."
        )
        desc.setWordWrap(True)
        desc.setStyleSheet(f"color: {COLORS['text_dim']}; font-size: 14px; margin-bottom: 20px;")
        layout.addWidget(desc)
        
        # --- Configuration Group ---
        config_group = QGroupBox("1. Scan Configuration")
        config_layout = QVBoxLayout(config_group)
        
        # Path Selection
        path_row = QHBoxLayout()
        self.linker_path_edit = QLineEdit()
        self.linker_path_edit.setPlaceholderText("Select a file or folder to analyze...")
        browse_btn = QPushButton("📂 Browse...")
        browse_btn.clicked.connect(lambda: self._browse_to_line_edit(self.linker_path_edit))
        path_row.addWidget(self.linker_path_edit)
        path_row.addWidget(browse_btn)
        config_layout.addLayout(path_row)
        
        # Options
        opts_layout = QHBoxLayout()
        self.link_recursive_check = QCheckBox("Recursive Scan")
        self.link_recursive_check.setChecked(True)
        self.link_all_check = QCheckBox("Link All Occurrences (Uncheck = First Only)")
        
        opts_layout.addWidget(self.link_recursive_check)
        opts_layout.addWidget(self.link_all_check)
        opts_layout.addStretch()
        config_layout.addLayout(opts_layout)
        
        # Scan Button
        self.scan_links_btn = QPushButton("🔎 Scan for Potential Links")
        self.scan_links_btn.setProperty("class", "primary")
        self.scan_links_btn.setMinimumHeight(40)
        self.scan_links_btn.clicked.connect(self._scan_links_dry_run_threaded)
        config_layout.addWidget(self.scan_links_btn)
        
        layout.addWidget(config_group)
        
        # --- Progress Section ---
        progress_group = QGroupBox("Status & Log")
        progress_layout = QVBoxLayout(progress_group)
        
        self.linker_progress = QProgressBar()
        self.linker_progress.setTextVisible(True)
        self.linker_progress.setFormat("%p% - %v/%m files")
        self.linker_progress.setVisible(False)
        progress_layout.addWidget(self.linker_progress)
        
        self.linker_log = QTextEdit()
        self.linker_log.setReadOnly(True)
        self.linker_log.setPlaceholderText("Detailed logs will appear here during scanning...")
        self.linker_log.setStyleSheet("font-family: Consolas, monospace; font-size: 12px; background-color: #1e1e1e; color: #d4d4d4;")
        self.linker_log.setMaximumHeight(200)
        progress_layout.addWidget(self.linker_log)
        
        layout.addWidget(progress_group)
        
        # --- Review Group ---
        review_group = QGroupBox("2. Review & Apply")
        review_layout = QVBoxLayout(review_group)
        
        # Table
        self.linker_table = QTableWidget()
        self.linker_table.setColumnCount(4)
        self.linker_table.setHorizontalHeaderLabels(["Key Term", "Found Count", "Target Link", "Apply?"])
        self.linker_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.linker_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        review_layout.addWidget(self.linker_table)
        
        # Controls
        ctrl_row = QHBoxLayout()
        sel_all_btn = QPushButton("Select All")
        sel_all_btn.clicked.connect(lambda: self._set_linker_checks(True))
        desel_all_btn = QPushButton("Deselect All")
        desel_all_btn.clicked.connect(lambda: self._set_linker_checks(False))
        
        ctrl_row.addWidget(sel_all_btn)
        ctrl_row.addWidget(desel_all_btn)
        ctrl_row.addStretch()
        
        self.apply_links_btn = QPushButton("✅ Apply Selected Links")
        self.apply_links_btn.setProperty("class", "success")
        self.apply_links_btn.setEnabled(False)
        self.apply_links_btn.clicked.connect(self._apply_selected_links_threaded)
        ctrl_row.addWidget(self.apply_links_btn)
        
        review_layout.addLayout(ctrl_row)
        layout.addWidget(review_group)
        layout.addStretch()

    def _browse_to_line_edit(self, line_edit):
        path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if path:
            line_edit.setText(path)

    def _set_linker_checks(self, checked: bool):
        """Helper to mass check/uncheck."""
        for row in range(self.linker_table.rowCount()):
            item = self.linker_table.cellWidget(row, 3)
            # Find checkbox in container
            chk = item.findChild(QCheckBox) if item else None
            if chk:
                chk.setChecked(checked)

    def _scan_links_dry_run_threaded(self):
        """Start the scan in a background thread."""
        path_str = self.linker_path_edit.text()
        if not path_str or not Path(path_str).exists():
            QMessageBox.warning(self, "Error", "Invalid path selected.")
            return

        # 1. Prepare UI
        self.linker_log.clear()
        self.linker_log.append("PREPARING SCAN...")
        self.linker_progress.setVisible(True)
        self.linker_progress.setValue(0)
        self.scan_links_btn.setEnabled(False)
        self.apply_links_btn.setEnabled(False)
        self.linker_table.setRowCount(0)
        
        # 2. Start Thread
        self._linker_thread = LinkerWorker(
            mode="scan",
            path=path_str,
            vault_path=self.settings.get('obsidian', 'vault_path', '.'),
            recursive=self.link_recursive_check.isChecked()
        )
        
        self._linker_thread.log_signal.connect(self._append_linker_log)
        self._linker_thread.progress_signal.connect(self._update_linker_progress)
        self._linker_thread.finished_scan_signal.connect(self._on_scan_finished)
        self._linker_thread.error_signal.connect(self._on_linker_error)
        
        self._linker_thread.start()

    def _apply_selected_links_threaded(self):
        """Start applying links in a background thread."""
        if not hasattr(self, '_files_to_link') or not self._files_to_link:
            return

        # Gather approved terms
        approved = []
        for row in range(self.linker_table.rowCount()):
            container = self.linker_table.cellWidget(row, 3)
            chk = container.findChild(QCheckBox)
            if chk and chk.isChecked():
                term = self.linker_table.item(row, 0).text()
                approved.append(term)
        
        if not approved:
            QMessageBox.information(self, "Info", "No terms selected to apply.")
            return

        # 1. Prepare UI
        self.linker_log.append("\nPREPARING TO APPLY LINKS...")
        self.linker_progress.setVisible(True)
        self.linker_progress.setValue(0)
        self.scan_links_btn.setEnabled(False)
        self.apply_links_btn.setEnabled(False)
        
        # 2. Start Thread
        self._linker_thread = LinkerWorker(
            mode="apply",
            vault_path=self.settings.get('obsidian', 'vault_path', '.'),
            files=self._files_to_link,
            approved_terms=approved,
            link_all=self.link_all_check.isChecked()
        )
        
        self._linker_thread.log_signal.connect(self._append_linker_log)
        self._linker_thread.progress_signal.connect(self._update_linker_progress)
        self._linker_thread.finished_apply_signal.connect(self._on_apply_finished)
        self._linker_thread.error_signal.connect(self._on_linker_error)
        
        self._linker_thread.start()

    # --- Worker Slots ---

    def _append_linker_log(self, msg: str):
        self.linker_log.append(msg)
        # Auto-scroll
        sb = self.linker_log.verticalScrollBar()
        sb.setValue(sb.maximum())

    def _update_linker_progress(self, current: int, total: int):
        self.linker_progress.setMaximum(total)
        self.linker_progress.setValue(current)

    def _on_scan_finished(self, global_counts: dict, files: list):
        self.scan_links_btn.setEnabled(True)
        self.linker_progress.setVisible(False)
        self._files_to_link = files
        
        # Populate Table
        self.linker_table.setRowCount(len(global_counts))
        sorted_items = sorted(global_counts.items(), key=lambda x: x[1], reverse=True)
        
        # Need to re-instantiate linker to get custom terms mapping solely for display
        # Creating a lightweight map for display. Thread already did the hard work.
        from engine.knowledge_acquisition_engine import AutoLinker
        linker = AutoLinker(Path("."))
        
        for row, (term, count) in enumerate(sorted_items):
            self.linker_table.setItem(row, 0, QTableWidgetItem(term))
            self.linker_table.setItem(row, 1, QTableWidgetItem(str(count)))
            
            target = linker.custom_terms.get(term, f"[[{term}]]")
            self.linker_table.setItem(row, 2, QTableWidgetItem(target))
            
            # Centered checkbox
            chk = QCheckBox()
            chk.setChecked(True)
            container = QWidget()
            l = QHBoxLayout(container)
            l.setContentsMargins(0,0,0,0)
            l.setAlignment(Qt.AlignmentFlag.AlignCenter)
            l.addWidget(chk)
            self.linker_table.setCellWidget(row, 3, container)
            
        self.apply_links_btn.setEnabled(True)
        self.linker_log.append(f"\n✅ SCAN COMPLETED. Found {len(global_counts)} terms.")

    def _on_apply_finished(self, total_links: int, files_mod: int):
        self.scan_links_btn.setEnabled(True)
        self.linker_progress.setVisible(False)
        self.linker_table.setRowCount(0) # Clear table
        
        QMessageBox.information(self, "Success", f"Operation Complete!\n\nModified {files_mod} files.\nCreated {total_links} new links.")
        self.linker_log.append(f"\n✅ APPLY COMPLETED. {total_links} links created.")

    def _on_linker_error(self, err_msg: str):
        self.scan_links_btn.setEnabled(True)
        self.apply_links_btn.setEnabled(True) # Maybe?
        self.linker_progress.setVisible(False)
        QMessageBox.critical(self, "Worker Error", err_msg)
        self.linker_log.append(f"❌ ERROR: {err_msg}")


# ==========================================
# WORKER THREAD
# ==========================================
from PySide6.QtCore import QThread, Signal

class LinkerWorker(QThread):
    log_signal = Signal(str)
    progress_signal = Signal(int, int)
    error_signal = Signal(str)
    
    # Results
    finished_scan_signal = Signal(dict, list) # counts, file_list
    finished_apply_signal = Signal(int, int)  # total_links, files_mod
    
    def __init__(self, mode: str, **kwargs):
        super().__init__()
        self.mode = mode
        self.kwargs = kwargs
        self._stops = False

    def run(self):
        try:
            from engine.knowledge_acquisition_engine import AutoLinker
            from collections import Counter
            
            vault_path = Path(self.kwargs.get('vault_path'))
            linker = AutoLinker(vault_path)
            
            if self.mode == "scan":
                path_str = self.kwargs.get('path')
                recursive = self.kwargs.get('recursive')
                path = Path(path_str)
                
                self.log_signal.emit(f"Scanning directory: {path}")
                
                # Gather files
                files = []
                if path.is_file():
                    files = [path]
                elif recursive:
                    files = list(path.rglob("*.md"))
                else:
                    files = list(path.glob("*.md"))
                    
                total = len(files)
                self.log_signal.emit(f"Found {total} files to scan.")
                
                global_counts = Counter()
                
                for i, f in enumerate(files):
                    # self.log_signal.emit(f"Scanning {f.name}...") 
                    # Don't log every single file unless slow, but user asked for "show me it working"
                    # We will log every 5 files or if it finds something noteworthy
                    
                    local_counts = linker.scan_file(f)
                    if len(local_counts) > 0:
                        count_str = ", ".join([f"{k}({v})" for k,v in list(local_counts.items())[:3]])
                        if len(local_counts) > 3: count_str += "..."
                        self.log_signal.emit(f"[{i+1}/{total}] {f.name}: Found {count_str}")
                    else:
                        if i % 10 == 0:
                            self.log_signal.emit(f"[{i+1}/{total}] {f.name}: No terms found.")

                    global_counts.update(local_counts)
                    self.progress_signal.emit(i+1, total)
                    
                self.finished_scan_signal.emit(dict(global_counts), files)
                
            elif self.mode == "apply":
                files = self.kwargs.get('files')
                approved = self.kwargs.get('approved_terms')
                link_all = self.kwargs.get('link_all')
                
                total = len(files)
                total_links = 0
                files_mod = 0
                
                self.log_signal.emit(f"Applying links for {len(approved)} terms across {total} files...")
                
                for i, f in enumerate(files):
                    count = linker.apply_links_to_file(f, approved, link_all=link_all)
                    if count > 0:
                        self.log_signal.emit(f"[{i+1}/{total}] {f.name}: +{count} links")
                        total_links += count
                        files_mod += 1
                    else:
                        # self.log_signal.emit(f"[{i+1}/{total}] {f.name}: Unchanged")
                        pass
                        
                    self.progress_signal.emit(i+1, total)
                    
                self.finished_apply_signal.emit(total_links, files_mod)
                
        except Exception as e:
            import traceback
            self.error_signal.emit(f"{str(e)}\n{traceback.format_exc()}")
    # ==========================================
    # PAGE 4: DEFINITIONS MANAGER
    # ==========================================
    def _build_definitions_page(self):
        """Build the definition scanner page."""
        page, layout = self._create_page_container("📖 Definition Scanner & Validator")
        
        # Two column layout
        columns = QHBoxLayout()
        
        # Left: Scanner controls
        left = QVBoxLayout()
        
        folder_group = QGroupBox("Definitions Folder")
        folder_layout = QVBoxLayout(folder_group)
        
        self.def_folder_path = QLineEdit()
        self.def_folder_path.setText(self._folder_config.get('glossary', ''))
        folder_layout.addWidget(self.def_folder_path)
        
        btn_row = QHBoxLayout()
        browse_btn = QPushButton("Browse...")
        browse_btn.clicked.connect(lambda: self._browse_to_line_edit(self.def_folder_path))
        btn_row.addWidget(browse_btn)
        
        use_glossary_btn = QPushButton("Use Glossary")
        use_glossary_btn.setProperty("class", "primary")
        use_glossary_btn.clicked.connect(lambda: self.def_folder_path.setText(
            self._folder_config.get('glossary', '')
        ))
        btn_row.addWidget(use_glossary_btn)
        folder_layout.addLayout(btn_row)
        
        self.def_recursive = QCheckBox("Scan recursively")
        self.def_recursive.setChecked(True)
        folder_layout.addWidget(self.def_recursive)
        
        left.addWidget(folder_group)
        
        # Scan buttons
        scan_group = QGroupBox("Scan & Validate")
        scan_layout = QVBoxLayout(scan_group)
        
        scan_defs_btn = QPushButton("🔍 SCAN DEFINITIONS")
        scan_defs_btn.setProperty("class", "success")
        scan_defs_btn.clicked.connect(self._scan_definitions)
        scan_layout.addWidget(scan_defs_btn)
        
        inject_btn = QPushButton("📝 INJECT TEMPLATES (Add Structure)")
        inject_btn.setProperty("class", "warning")
        scan_layout.addWidget(inject_btn)
        
        run_engine_btn = QPushButton("⚡ RUN ENGINE (Auto-Fill All)")
        run_engine_btn.setProperty("class", "purple")
        scan_layout.addWidget(run_engine_btn)
        
        dry_run = QCheckBox("Dry run (preview only, no changes)")
        scan_layout.addWidget(dry_run)
        
        left.addWidget(scan_group)
        
        # Stats
        stats_group = QGroupBox("Statistics")
        stats_layout = QVBoxLayout(stats_group)
        self.def_stats_label = QLabel("No scan performed yet")
        self.def_stats_label.setStyleSheet(f"color: {COLORS['text_muted']};")
        stats_layout.addWidget(self.def_stats_label)
        left.addWidget(stats_group)
        
        left.addStretch()
        columns.addLayout(left, 1)
        
        # Right: Definition details
        right = QVBoxLayout()
        
        details_group = QGroupBox("Definition Details")
        details_layout = QVBoxLayout(details_group)
        
        # Term
        term_row = QHBoxLayout()
        term_row.addWidget(QLabel("Term:"))
        self.def_term_edit = QLineEdit()
        term_row.addWidget(self.def_term_edit)
        details_layout.addLayout(term_row)
        
        # Completeness meter would go here
        details_layout.addWidget(QLabel("Completeness: ---"))
        
        # Missing sections
        missing_group = QGroupBox("⚠️ Missing Sections")
        missing_layout = QVBoxLayout(missing_group)
        missing_layout.addWidget(QLabel("Select a definition to see what's missing"))
        details_layout.addWidget(missing_group)
        
        # Section checklist
        checklist_group = QGroupBox("Section Checklist")
        checklist_layout = QVBoxLayout(checklist_group)
        
        sections = [
            "1. Canonical Definition",
            "2. Axioms",
            "3. Mathematical Structure",
            "4. Domain Interpretations",
            "5. Operationalization",
            "6. Failure Modes",
            "7. Integration Map",
            "8. Usage Drift Log",
            "9. External Comparison",
            "10. Notes & Examples"
        ]
        for section in sections:
            cb = QCheckBox(section)
            checklist_layout.addWidget(cb)
        
        details_layout.addWidget(checklist_group)
        
        # Editor
        editor_group = QGroupBox("Content Editor")
        editor_layout = QVBoxLayout(editor_group)
        self.def_content_editor = QTextEdit()
        self.def_content_editor.setPlaceholderText("Select a definition to edit...")
        editor_layout.addWidget(self.def_content_editor)
        
        btn_row = QHBoxLayout()
        save_btn = QPushButton("💾 Save Changes")
        save_btn.setProperty("class", "success")
        btn_row.addWidget(save_btn)
        
        open_btn = QPushButton("📂 Open in Explorer")
        btn_row.addWidget(open_btn)
        editor_layout.addLayout(btn_row)
        
        details_layout.addWidget(editor_group)
        
        right.addWidget(details_group)
        columns.addLayout(right, 2)
        
        layout.addLayout(columns)
    
    def _browse_to_line_edit(self, edit: QLineEdit):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", edit.text())
        if folder:
            edit.setText(folder)
    
    def _scan_definitions(self):
        """Scan definitions folder."""
        path = self.def_folder_path.text()
        if not path or not Path(path).exists():
            QMessageBox.warning(self, "No Folder", "Please select a valid definitions folder.")
            return
        
        self.definitions_manager.set_vault_path(Path(path).parent)
        defs = self.definitions_manager.scan_definitions()
        count = len(self.definitions_manager.get_all_definitions())
        
        self.def_stats_label.setText(f"Found {count} definitions in {len(defs)} files")
        QMessageBox.information(self, "Scan Complete", f"Found {count} definitions!")
    
    # ==========================================
    # Remaining pages (simplified placeholders)
    # ==========================================
    def _build_definitions_page(self):
        page, layout = self._create_page_container("📚 Definitions Manager")
        layout.addWidget(QLabel("Manage your full definitions library here. (Placeholder)"))
        layout.addStretch()
        layout.addStretch()
    
    def _build_vault_system_page(self):
        page, layout = self._create_page_container("🏗️ Vault System")
        layout.addWidget(QLabel("Import VaultSystemTab here"))
        layout.addStretch()
    
    def _build_aggregation_page(self):
        page, layout = self._create_page_container("📊 Data Aggregation")
        layout.addWidget(QLabel("Import DataAggregationTab here"))
        layout.addStretch()
    
    def _build_research_links_page(self):
        page, layout = self._create_page_container("🔗 Research Links")
        layout.addWidget(QLabel("Import ResearchLinkingTab here"))
        layout.addStretch()
    
    def _build_footnotes_page(self):
        page, layout = self._create_page_container("📝 Footnotes")
        layout.addWidget(QLabel("Import FootnoteTab here"))
        layout.addStretch()
    
    def _build_database_page(self):
        page, layout = self._create_page_container("🗄️ Database")
        layout.addWidget(QLabel("Import DatabaseTab here"))
        layout.addStretch()
    
    def _build_settings_page(self):
        page, layout = self._create_page_container("⚙️ Settings")
        
        # API Keys
        api_group = QGroupBox("API Configuration")
        api_layout = QVBoxLayout(api_group)
        
        # OpenAI
        row = QHBoxLayout()
        row.addWidget(QLabel("OpenAI API Key:"))
        self.openai_key_edit = QLineEdit()
        self.openai_key_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.openai_key_edit.setText(self.settings.get('openai', 'api_key', ''))
        row.addWidget(self.openai_key_edit)
        api_layout.addLayout(row)
        
        # Claude
        row = QHBoxLayout()
        row.addWidget(QLabel("Claude API Key:"))
        self.claude_key_edit = QLineEdit()
        self.claude_key_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.claude_key_edit.setText(self.settings.get('claude', 'api_key', ''))
        row.addWidget(self.claude_key_edit)
        api_layout.addLayout(row)
        
        layout.addWidget(api_group)
        
        # Save
        save_btn = QPushButton("💾 Save Settings")
        save_btn.setProperty("class", "primary")
        save_btn.clicked.connect(self._save_settings)
        layout.addWidget(save_btn)
        
        layout.addStretch()
    
    def _save_settings(self):
        """Save settings."""
        self.settings.set('openai', 'api_key', self.openai_key_edit.text())
        self.settings.set('claude', 'api_key', self.claude_key_edit.text())
        self.settings.save()
        QMessageBox.information(self, "Saved", "Settings saved!")
    
    def _setup_status_bar(self):
        """Setup status bar."""
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")
        
        vault = self._folder_config.get('vault_root', '')
        if vault:
            self.status_bar.showMessage(f"Vault: {Path(vault).name}")


def create_main_window_v2(
    settings,
    definitions_manager,
    vault_installer,
    global_aggregator,
    research_linker,
    footnote_system,
    postgres_manager
) -> MainWindowV2:
    """Factory function to create the V2 main window."""
    return MainWindowV2(
        settings=settings,
        definitions_manager=definitions_manager,
        vault_installer=vault_installer,
        global_aggregator=global_aggregator,
        research_linker=research_linker,
        footnote_system=footnote_system,
        postgres_manager=postgres_manager
    )
