local monitor = peripheral.find("monitor")
print(monitor)
local old = term.redirect(monitor)

local xScale, yScale = monitor.getSize()

local left = 0.5 -- left paddle y
local right = 0.5 -- right paddle y
local pos = vector.new(0.5, 0.5) -- ballpos
local velocity = vector.new(math.random(0.01), math.random(0.01)) -- ball velocity

local function round(x, n)
    -- n places after decimal
    n = 10^n
    if math.abs(x*n -math.floor(x*n)) > math.abs(x*n -math.ceil(x*n)) then
        return math.ceil(x*n)/n
    else
        return math.floor(x*n)/n
    end
end

local running = true
while running do
    -- move ball
    pos[0] = pos[0] + velocity[0]
    pos[1] = pos[1] + velocity[1]

    -- input
    local event, key = os.pullEvent("key")
    if key == 83 then
        -- down
        left = left + 0.01
    end

    if key == 87 then
        -- up
        left = left - 0.01
    end

    -- bad ai
    if pos[1] > right then
        right = right + 0.01
    else
        right = right - 0.01
    end

    -- bounce
    -- paddles
    if velocity[0] > 0 then
        if round(pos[0], 1) == 0.1 and round(left, 1) == round(pos[1], 1) then
            velocity[0] = velocity[0] * -1.1
            velocity[1] = 2*velocity[1] - left
        end
    else
        if round(pos[0], 1) == 0.9 and round(right, 1) == round(pos[1], 1) then
            velocity[0] = velocity[0] * -1.1
            velocity[1] = 2*velocity[1] - right
        end
    end

    -- roof/floor
    if pos[1] < 0 or pos[1] > 1 then
        velocity[1] = velocity[1] * -1
    end

    -- death
    if pos[0] > 1 or pos[0] < 0 then
        running = false
    end

    -- draw
    -- paddles
    paintutils.drawLine(xScale*0.1, yScale*(left+0.1), xScale*0.9, yScale*(left-0.1), colors.white)
    paintutils.drawLine(xScale*0.1, yScale*(right+0.1), xScale*0.9, yScale*(right-0.1), colors.white)
    
    -- ball
    paintutils.drawPixel(pos[0], pos[1], colors.white)
end