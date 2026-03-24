from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_mood_trail_basic_functionality():
    driver = webdriver.Chrome()
    try:
        # Load the app
        driver.get('http://localhost:8000')
        
        # Test wheel interaction
        wheel = driver.find_element(By.ID, 'wheelCanvas')
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(wheel, 150, 150).click().perform()
        
        # Test note input
        note_input = driver.find_element(By.CLASS_NAME, 'mood-note')
        note_input.send_keys('Feeling great today!')
        
        # Test save functionality
        save_button = driver.find_element(By.CLASS_NAME, 'save-btn')
        save_button.click()
        
        # Verify local storage
        mood_history = driver.execute_script('return localStorage.getItem("moodHistory")')
        assert mood_history is not None
        
        # Verify trail canvas updated
        trail_canvas = driver.find_element(By.ID, 'trailCanvas')
        assert trail_canvas.is_displayed()
        
        print('All tests passed!')
        
    finally:
        driver.quit()

if __name__ == '__main__':
    test_mood_trail_basic_functionality()