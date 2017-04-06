require 'mongo'
require 'json'
require 'pp'

client = Mongo::Client.new([ 'ds147777.mlab.com:47777' ], :database => 'tripper', user: 'showntop', password: 'xrt310214@tz')

ch = {}
client[:categories].find().each{|c| ch[c['name']] = c['_id'] }
pp ch

ct_array = []
pt_array = []
File.readlines('./sunnder/items.json').each do |line|
	item = JSON.parse(line)
	ct = item['category']
	ct = '无分类' if ct == nil
	if !ch.keys.include?(ct)
		ch[ct] = ch.values.size + 1
		ct_array << {"_id": ch.values.size, "name": ct}
		# client[:categories].insert_one()
	end
	if item['title'] == nil || item['content'] == ""
		next
	end
	ob = { :title => item['title'], category: ch[ct], asset: item['image_urls'].fetch(0, nil), content: item['content'] }
	pt_array << ob
    # client[:projects].insert_one(ob )
end
client[:categories].insert_many(ct_array)
client[:projects].insert_many(pt_array)
# pp ct_array
# pp pt_array

