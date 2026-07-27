package com.storytime.android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.AnimatedContentTransitionScope
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.ColorFilter
import androidx.compose.ui.unit.dp
import androidx.navigation.NavDestination.Companion.hierarchy
import androidx.navigation.NavGraph.Companion.findStartDestination
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.storytime.android.ui.CatalogScreen
import com.storytime.android.ui.CreateStoryScreen
import com.storytime.android.ui.EndingsGridScreen
import com.storytime.android.ui.LegalPage
import com.storytime.android.ui.LegalPageScreen
import com.storytime.android.ui.LibraryScreen
import com.storytime.android.ui.OnboardingScreen
import com.storytime.android.ui.ProfileScreen
import com.storytime.android.ui.SettingsScreen
import com.storytime.android.ui.StoryReaderScreen
import com.storytime.android.ui.StoryStartScreen
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.StoryTimeTheme
import com.storytime.android.ui.theme.DoodleIcon

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            val settings by app.settings.state.collectAsState()
            StoryTimeTheme(settings) { Root() }
        }
    }
}

private data class TabSpec(val route: String, val label: String, val doodle: String)

private val tabs = listOf(
    TabSpec("catalog", "Discover", "clapperboard"),
    TabSpec("library", "Library",  "bookmark"),
    TabSpec("create",  "Create",   "plus"),
    TabSpec("profile", "Profile",  "person"),
    TabSpec("settings","Settings", "gear"),
)

// Precomputed once so the tab-visibility check isn't allocating a list on
// every recomposition of Root().
private val tabRoutes: Set<String> = tabs.map { it.route }.toSet()

@Composable
private fun Root() {
    val profile by app.user.profile.collectAsState()
    val nav = rememberNavController()
    val palette = LocalStPalette.current

    if (!profile.onboardingCompleted) {
        OnboardingScreen(onDone = {
            app.user.update { it.copy(onboardingCompleted = true) }
        })
        return
    }

    val backStack by nav.currentBackStackEntryAsState()
    val currentRoute = backStack?.destination?.route
    val showTabs = currentRoute in tabRoutes

    Scaffold(
        containerColor = palette.paper,
        bottomBar = {
            if (showTabs) NavigationBar(containerColor = palette.butter) {
                tabs.forEach { tab ->
                    val selected = backStack?.destination?.hierarchy?.any { it.route == tab.route } == true
                    NavigationBarItem(
                        selected = selected,
                        onClick = {
                            nav.navigate(tab.route) {
                                popUpTo(nav.graph.findStartDestination().id) { saveState = true }
                                launchSingleTop = true
                                restoreState = true
                            }
                        },
                        icon = {
                            DoodleIcon(
                                tab.doodle,
                                modifier = Modifier.size(24.dp),
                                tint = ColorFilter.tint(if (selected) palette.ink else palette.inkSoft),
                            )
                        },
                        label = { Text(tab.label) },
                        colors = NavigationBarItemDefaults.colors(
                            selectedIconColor = palette.ink,
                            unselectedIconColor = palette.inkSoft,
                            selectedTextColor = palette.ink,
                            unselectedTextColor = palette.inkSoft,
                            indicatorColor = Color.Transparent,
                        ),
                    )
                }
            }
        },
    ) { padding ->
        Box(Modifier.fillMaxSize().padding(padding).background(palette.paper)) {
            NavHost(
                navController = nav,
                startDestination = "catalog",
                // The reference recenters the selected cover into a detail
                // slot. A short slide/fade gives native routes the same
                // continuous handoff without replacing Compose navigation.
                enterTransition = {
                    slideIntoContainer(
                        AnimatedContentTransitionScope.SlideDirection.Start,
                        animationSpec = tween(420),
                    ) + fadeIn(animationSpec = tween(260))
                },
                exitTransition = {
                    slideOutOfContainer(
                        AnimatedContentTransitionScope.SlideDirection.Start,
                        animationSpec = tween(320),
                    ) + fadeOut(animationSpec = tween(220))
                },
                popEnterTransition = {
                    slideIntoContainer(
                        AnimatedContentTransitionScope.SlideDirection.End,
                        animationSpec = tween(360),
                    ) + fadeIn(animationSpec = tween(240))
                },
                popExitTransition = {
                    slideOutOfContainer(
                        AnimatedContentTransitionScope.SlideDirection.End,
                        animationSpec = tween(300),
                    ) + fadeOut(animationSpec = tween(200))
                },
            ) {
                composable("catalog") {
                    CatalogScreen(onPick = { id -> nav.navigate("start/$id") })
                }
                composable("library") {
                    LibraryScreen(onPick = { id -> nav.navigate("start/$id") })
                }
                composable("create") {
                    CreateStoryScreen(onCreated = { id -> nav.navigate("start/$id") })
                }
                composable("profile") {
                    ProfileScreen(onSeeEndings = { id -> nav.navigate("endings/$id") })
                }
                composable("settings") {
                    SettingsScreen(onLegal = { page -> nav.navigate("legal/${page.name}") })
                }
                composable("legal/{page}") { entry ->
                    val page = runCatching { LegalPage.valueOf(entry.arguments?.getString("page") ?: "") }
                        .getOrDefault(LegalPage.About)
                    LegalPageScreen(page = page, onBack = { nav.popBackStack() })
                }
                composable("start/{id}") { entry ->
                    val id = entry.arguments?.getString("id").orEmpty()
                    StoryStartScreen(
                        storyId = id,
                        onBegin = { nav.navigate("reader/$id") },
                        onResume = { nodeId -> nav.navigate("reader/$id?node=$nodeId") },
                        onBack = { nav.popBackStack() },
                        onSeeEndings = { nav.navigate("endings/$id") },
                    )
                }
                composable(
                    route = "reader/{id}?node={node}",
                    arguments = listOf(
                        navArgument("id") { type = NavType.StringType },
                        navArgument("node") { type = NavType.StringType; nullable = true; defaultValue = null },
                    ),
                ) { entry ->
                    val id = entry.arguments?.getString("id").orEmpty()
                    val node = entry.arguments?.getString("node")
                    StoryReaderScreen(
                        storyId = id,
                        resumeNodeId = node,
                        onExit = { nav.popBackStack("catalog", inclusive = false) },
                        onContinueSaga = { nextId ->
                            nav.popBackStack("catalog", inclusive = false)
                            nav.navigate("start/$nextId")
                        },
                    )
                }
                composable("endings/{id}") { entry ->
                    val id = entry.arguments?.getString("id").orEmpty()
                    EndingsGridScreen(storyId = id, onBack = { nav.popBackStack() })
                }
            }
        }
    }
}
